from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from account.utils import prepare_context
from schedule.models import Station
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

        user = User.objects.get(username=request.user.username)
        acconut = Account.objects.get(user_id=user)
        print(account)
        ticket_info = map(int, request.POST.get('selectedTicket').split('-'))

        Ticket()
        if request.POST.get('paymentMethod'):
            return render(request, 'booking/successfulBooking.html', context=context)
        else:
            return render(request, 'booking/selectTransaction.html', context=context)
