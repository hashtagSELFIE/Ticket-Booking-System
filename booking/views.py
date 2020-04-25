from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class FindSchedule(View):
    def get(self, request):
        context = {'show_navbar': True}
        return render(request, 'booking/searchSchedule.html', context=context)

    def post(self, request):
        context = {'show_navbar': True, 'schedule': {
            'from': request.POST.get('from'), 'to': request.POST.get('to')}}
        return render(request, 'booking/searchSchedule.html', context=context)


class SelectTransaction(View):
    def get(self, request):
        context = {'show_navbar': True}
        return redirect('booking/schedules/')

    def post(self, request):
        context = {'show_navbar': True}
        if request.POST.get('paymentMethod'):
            return render(request, 'booking/successfulBooking.html', context=context)
        else:
            return render(request, 'booking/selectTransaction.html', context=context)
