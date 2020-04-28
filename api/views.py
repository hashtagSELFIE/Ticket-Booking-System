import json
from django.core import serializers
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.db.models.functions import Concat
from django.db.models import CharField, Value as V
from schedule.models import Station, Timetable, Train


# Create your views here.
def fetch_schedules(request):
    if request.method == 'GET':
        from_st = request.GET.get('from')
        to_st = request.GET.get('to')

        schedules = []
        if not (from_st and to_st):
            for train in Train.objects.all():
                train_timetable = Timetable.objects.filter(
                    train_id=train.id)
                schedules.append({
                    train.id: {
                        'train_name': train.train_name,
                        'timetable': serializers.serialize('json', train_timetable, fields=('station', 'arrived_time', 'departed_time'))
                    }
                })
        else:
            train_filter = Timetable.objects.filter(
                station_id__in=[from_st, to_st]).values('train_id')

            train_filter_id = set([t['train_id'] for t in train_filter])
            for train in Train.objects.filter(id__in=train_filter_id):
                train_timetable = Timetable.objects.filter(
                    train_id=train.id)
                schedules.append({
                    train.id: {
                        'train_name': train.train_name,
                        'timetable': serializers.serialize('json', train_timetable, fields=('station', 'arrived_time', 'departed_time'))
                    }
                })
        return JsonResponse(schedules, content_type='application/json', safe=False)
    return HttpResponse("bad request", status=400)
