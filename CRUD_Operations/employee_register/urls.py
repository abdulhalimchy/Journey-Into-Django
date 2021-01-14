from django.contrib import admin
from django.urls import path, include
from employee_register import views

urlpatterns = [
    path('', views.employe_form, name="employee_form"),
    path('list/', views.employe_list, name="employee_list"),
    path('delete/', views.employe_delete, name="employee_delete"),
]