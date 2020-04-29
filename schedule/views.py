from django.shortcuts import render
from django.views import View
from schedule.models import Timetable, Train, Station
from django.db.models import Q
from account.utils import prepare_context

# Create your views here.


class SearchTimetable(View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        context['train'] = Train.objects.all()
        context['timetable'] = Timetable.objects.all()
        context['stations'] = Station.objects.all()
        return render(request, 'schedule/searchTimetable.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        context['timetable'] = Timetable.objects.filter()

        from_st = request.POST.get('from')
        to_st = request.POST.get('to')

        if from_st != to_st:
            timetables = []
            train_filter = Timetable.objects.filter(
                Q(station_id__in=[from_st, to_st])).values('train_id')
            train_filter_id = set([t['train_id'] for t in train_filter])
            for train in Train.objects.filter(id__in=train_filter_id):
                train_timetable = Timetable.objects.filter(
                    train_id__exact=train.id)
                from_filter = train_timetable.filter(station_id=from_st)
                to_filter = train_timetable.filter(station_id=to_st)

                if (from_filter != None and to_filter != None and len(from_filter) > 0 and len(to_filter) > 0):
                    if (from_filter[0].departed_time and to_filter[0].arrived_time and from_filter[0].departed_time < to_filter[0].arrived_time):
                        timetables.append({
                            'train': train,
                            'schedule': {
                                'from': from_filter[0],
                                'to': to_filter[0]
                            }
                        })
            context['timetables'] = timetables
            context['stations'] = Station.objects.all()
            context['schedule'] = {
                'from': Station.objects.get(pk=from_st),
                'to': Station.objects.get(pk=to_st)
            }
        else:
            context['train'] = Train.objects.all()
            context['timetable'] = Timetable.objects.all()
            context['stations'] = Station.objects.all()
            context['error'] = {
                'errorMsg': 'Please select different stations.'
            }

        return render(request, 'schedule/searchTimetable.html', context=context)
