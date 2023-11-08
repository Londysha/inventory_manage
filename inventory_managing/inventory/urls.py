from django.contrib import admin
from django.urls import path
from .views import InputDataView, DashboardView

urlpatterns = [
    path("input_data/", InputDataView.as_view(), name='input_data'),
    path("dashboard/", DashboardView.as_view(), name='dashboard'),
]
