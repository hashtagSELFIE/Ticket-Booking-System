from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.FindSchedule.as_view(), name="searchSchedules"),
    path('payments/', views.SelectTransaction.as_view(), name="selectTransaction")
]
