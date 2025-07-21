from django.contrib import admin
from django.urls import path
from . import views

app_name = 'lector'

urlpatterns = [
    path('prestamo/add/', views.RegistrarPrestamo.as_view(), name='prestamo-add'),
    path('prestamo/add2/', views.AddPrestamo.as_view(), name='prestamo-add2'),
    path('error/', views.ErrorView.as_view(), name='error'),
    path('prestamo/multiple-add/', views.AddMultiplePrestamo.as_view(), name='prestamo-add-multiple'),
]