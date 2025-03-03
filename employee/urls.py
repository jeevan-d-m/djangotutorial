from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:employee_id>/", views.employee_detail, name="employee_detail"),
]