import datetime
from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    """"Managers para el modelo Libro"""
    def listar_libros(self, kword):
        resultado = self.filter(titulo__icontains=kword, fecha__range=('1800-01-01','2020-01-01'))
        return resultado
    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(titulo__trigram_similar=kword)
        else:
            resultado = self.all()[:10]
        return resultado
    def listar_libros2(self, kword, f1, f2):
        fecha1 = datetime.datetime.strptime(f1, '%Y-%m-%d')
        fecha2 = datetime.datetime.strptime(f2, '%Y-%m-%d')
        resultado = self.filter(titulo__icontains=kword, fecha__range=(fecha1,fecha2))
        return resultado
    def listar_libros_categoria(self, categoria):
        resultado = self.filter(categoria__id=categoria).order_by('titulo')
        return resultado
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro
    def remove_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.remove(autor)
        return libro
    def libros_num_prestamos(self):
        resultado = self.aggregate(num_prestamos=Count('libro_prestamo'))
        return resultado
    def num_libros_prestados(self):
        resultado = self.annotate(num_prestados=Count('libro_prestamo '))
        for r in resultado:
            print('****************')
            print(r, r.num_prestados)
        return resultado

class CategoriaManager(models.Manager):
    """"Managers para el modelo Categoria"""
    def categoria_por_autor(self, autor):
        resultado = self.filter(categoria_libro__autores__id=autor).distinct()
        return resultado
    def listar_categoria_libros(self):
        resultado = self.annotate(num_libros=Count('categoria_libro'))
        for r in resultado:
            print('**************')
            print(r, r.num_libros)
        return resultado



