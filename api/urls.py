from django.urls import path
from . import views

urlpatterns = [
    path('getSchedules/', views.fetch_schedules),
]
