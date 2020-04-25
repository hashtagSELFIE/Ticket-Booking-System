from django.shortcuts import render
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
