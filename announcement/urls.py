from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewAnnouncement.as_view(), name="viewAnnouncement"),
    path('create/', views.CreateAnnouncement.as_view(), name="createAnnouncement"),
    path('edit/<int:announcement_id>/', views.EditAnnouncement.as_view(), name="editAnnouncement"),
    path('delete/<int:announcement_id>/', views.DeleteAnnouncement, name="deleteAnnouncement")
]
