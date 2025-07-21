from django.shortcuts import render
from django.views.generic import ListView, DetailView

# local models
from .models import Libro, Categoria

# Create your views here.
class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        #fecha 1
        f1 = self.request.GET.get("fecha1", '')
        #fecha 2
        f2 = self.request.GET.get("fecha2", '')

        if f1 and f2:
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)

class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Libro.objects.listar_libros_trg(palabra_clave)

class ListLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria('1')

class ListCategoria(ListView):
    context_object_name = 'lista_categorias'
    template_name = 'libro/lista3.html'

    def get_queryset(self):
        id_autor = self.request.GET.get("kword", '')
        if id_autor:
            return Categoria.objects.categoria_por_autor(int(id_autor))
        else:
            return Categoria.objects.categoria_por_autor('1')

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'


