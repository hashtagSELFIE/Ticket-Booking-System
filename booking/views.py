from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from account.utils import prepare_context


# Create your views here.
class FindSchedule(LoginRequiredMixin, View):
    login_required = True

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
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
        if request.POST.get('paymentMethod'):
            return render(request, 'booking/successfulBooking.html', context=context)
        else:
            return render(request, 'booking/selectTransaction.html', context=context)
