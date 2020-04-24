from django.contrib import admin
from schedule.models import Timetable, Station, Train

# Register your models here.
admin.site.register(Timetable)

admin.site.register(Station)

admin.site.register(Train)
