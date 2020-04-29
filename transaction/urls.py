from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewTransaction.as_view(), name="viewTransaction"),
    path('edit/<int:ticket_id>/', views.EditTransaction.as_view(), name="editTransaction"),
    path('delete/<int:ticket_id>/', views.DeleteTransaction, name="deleteTransaction")
]
