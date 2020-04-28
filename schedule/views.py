from django.shortcuts import render
from django.views import View
from schedule.models import Timetable, Train, Station
from account.utils import prepare_context

# Create your views here.


class SearchTimetable(View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        context['train'] = Train.objects.all()
        context['timetable'] = Timetable.objects.all()
        context['station'] = Station.objects.all()
        return render(request, 'schedule/searchTimetable.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        context['train'] = Train.objects.all()
        context['timetable'] = Timetable.objects.all()
        context['station'] = Station.objects.all()
        context['schedule'] = {
            'from': request.POST.get('from'),
            'to': request.POST.get('to')
        }
        return render(request, 'schedule/searchTimetable.html', context=context)
