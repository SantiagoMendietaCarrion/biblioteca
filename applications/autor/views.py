from django.shortcuts import render
from django.views.generic import ListView

# local models
from .models import Autor

# Create your views here.
class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Autor.objects.buscar_autor5(palabra_clave)


