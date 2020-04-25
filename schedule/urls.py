from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchTimetable.as_view(), name="searchTimetable")
]
