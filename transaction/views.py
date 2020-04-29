from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from account.utils import prepare_context
from account.models import Account
from booking.models import Ticket
from schedule.models import Timetable, Station, Train


class ViewTransaction(LoginRequiredMixin, View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = request.user
        context['user'] = user
        account = Account.objects.get(user_id_id=user.id)
        if account.user_type == 'TS':
            context['ticket'] = Ticket.objects.all()
            context['is_TS'] = True
        else:
            context['ticket'] = Ticket.objects.filter(buyer_id=account.id)

        context['schedule'] = Timetable.objects.all()
        context['station'] = Station.objects.all()
        context['train'] = Train.objects.all()

        return render(request, 'transaction/viewTransaction.html', context=context)

    def post(self, request):
        return HttpResponse(200)


class EditTransaction(LoginRequiredMixin, View):
    def get(self, request, ticket_id):
        context = prepare_context(request, show_navbar=True)
        context['ticket'] = Ticket.objects.get(pk=ticket_id)
        return render(request, 'transaction/editTransaction.html', context=context)

    def post(self, request, ticket_id):
        context = prepare_context(request, show_navbar=True)
        ticket = Ticket.objects.get(pk=ticket_id)
        transaction_information = request.POST.get('transaction_information')
        transaction_status = request.POST.get('transaction_status')
        booking_status = request.POST.get('booking_status')

        ticket.transactionInformation = transaction_information
        ticket.transactionStatus = HTMLCheckboxToBoolean(transaction_status)
        ticket.bookingStatus = HTMLCheckboxToBoolean(booking_status)

        ticket.save()

        return redirect('/transaction')


@login_required()
def DeleteTransaction(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def HTMLCheckboxToBoolean(a):
    if a is None:
        return False
    else:
        return True
