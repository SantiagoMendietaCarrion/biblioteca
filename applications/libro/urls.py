from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-2/', views.ListLibros2.as_view(), name='libros2'),
    path('categorias/', views.ListCategoria.as_view(), name='categorias'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name='detalle'),
    path('libro-trg/', views.ListLibrosTrg.as_view(), name='libros-trg'),
]