from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/confirmation/<int:appointment_id>/', views.appointment_confirmation, name='appointment_confirmation'),
    path('service-details/', views.service_detail, name='service_detail'),
    path('starter-page/', views.starter, name='starter'),
]
