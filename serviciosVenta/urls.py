from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('venta/', views.venta),
    path('servicios/', views.servicios),
]

