from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from account.utils import prepare_context
from schedule.models import Station, Timetable, Train
from .models import Ticket
from account.models import Account


# Create your views here.
class FindSchedule(LoginRequiredMixin, View):
    login_required = True

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        context['stations'] = Station.objects.all()
        return render(request, 'booking/searchSchedule.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        context['schedule'] = {
            'from': request.POST.get('from'),
            'to': request.POST.get('to')
        }
        return render(request, 'booking/searchSchedule.html', context=context)


class SelectTransaction(LoginRequiredMixin, View):
    login_required = True

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        return redirect('booking/schedules/')

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        context['selectedTicket'] = request.POST.get('selectedTicket')

        if request.POST.get('paymentMethod'):
            payment_method = request.POST.get('paymentMethod')
            user = User.objects.get(username=request.user.username)
            account = Account.objects.get(user_id=user)
            ticket_info = list(
                map(int, request.POST.get('selectedTicket').split('-')))

            ticket = Ticket.objects.create(
                buyer=account,
                boardingTrain=Train.objects.get(pk=ticket_info[0]),
                fromStation=Timetable.objects.get(pk=ticket_info[1]),
                toStation=Timetable.objects.get(pk=ticket_info[2]),
                transactionInformation=payment_method,
                transactionStatus=False,
                bookingStatus=False
            )
            # print(payment_method, ticket)
            context['ticket'] = ticket
            return redirect('selectTransaction', ticket_id=ticket.id)
        else:
            return render(request, 'booking/selectTransaction.html', context=context)


class BookingHistory(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'booking.view_ticket'

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = User.objects.get(username=request.user.username)
        account = Account.objects.get(user_id=user)
        print(account.user_type)
        is_TS = account.user_type == 'TS'
        context['is_TS'] = is_TS

        if is_TS:
            tickets = Ticket.objects.all().order_by("-buyDate")
            context['ticket'] = tickets
        else:
            tickets = Ticket.objects.filter(buyer=account).order_by("-buyDate")
            context['ticket'] = tickets
        return render(request, 'booking/historyBooking.html', context=context)


@login_required
def successful_booking(request, ticket_id):
    context = prepare_context(request, show_navbar=True)
    ticket = Ticket.objects.get(id=ticket_id)
    user = User.objects.get(username=request.user.username)
    account = Account.objects.get(user_id=user)

    if ticket.buyer.id != account.id:
        return redirect('/')
    else:
        context['ticket'] = ticket
        return render(request, 'booking/successfulBooking.html', context=context)


@login_required
@permission_required('booking.delete_ticket')
def cancel_booking(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()

    return redirect('/booking/history')
