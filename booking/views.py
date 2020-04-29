from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
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


class BookingHistory(LoginRequiredMixin, View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = User.objects.get(username=request.user.username)
        account = Account.objects.get(user_id=user)
        tickets = Ticket.objects.filter(buyer=account).order_by("-buyDate"),
        if tickets:
            ticket = {}
            for t in tickets[0]:
                if t.buyDate in ticket.keys():
                    ticket[t.buyDate].append(t)
                else:
                    ticket[t.buyDate] = [t]
            print(ticket)
            context['ticket'] = ticket
            print(context['ticket'])
        return render(request, 'booking/historyBooking.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        user = User.objects.get(username=request.user.username)
        account = Account.objects.get(user_id=user)
        tickets = Ticket.objects.filter(buyer=account).order_by("-buyDate"),
        if tickets:
            context['ticket'] = list(map(lambda t: t, tickets[0]))
            print(context['ticket'])
        return render(request, 'booking/historyBooking.html', context=context)


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
