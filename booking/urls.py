from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.FindSchedule.as_view(), name="searchSchedules"),
    path('payments/', views.SelectTransaction.as_view(), name="selectTransaction"),
    path('payments/success/<int:ticket_id>',
         views.successful_booking, name="selectTransaction")
]
