from django.shortcuts import render

# Create your views here.
from django.views import View
from schedule.models import Timetable, Train, Station


class SearchTimetable(View):
    def get(self, request):
        context = {'show_navbar': True,
                   'train': Train.objects.all(),
                   'timetable': Timetable.objects.all(),
                   'station': Station.objects.all()}
        return render(request, 'schedule/searchTimetable.html', context=context)

    def post(self, request):
        context = {'show_navbar': True, 'schedule': {
            'from': request.POST.get('from'), 'to': request.POST.get('to')}}
        return render(request, 'schedule/searchTimetable.html', context=context)
