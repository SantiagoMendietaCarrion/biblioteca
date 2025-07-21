from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """"Managers para el modelo Autor"""
    def listar_autores(self):
        return self.all
    def buscar_autor(self, kword):
        resultado = self.filter(nombres__icontains=kword)
        return resultado
    def buscar_autor2(self, kword):
        resultado = self.filter(Q(nombres__icontains=kword) | Q(apellidos__icontains=kword))
        return resultado
    def buscar_autor3(self, kword):
        resultado = self.filter(nombres__icontains=kword).filter(Q(edad__icontains=82) | Q(edad__icontains=87))
        return resultado
    def buscar_autor4(self, kword):
        resultado = self.filter(nombres__icontains=kword).exclude(Q(edad__icontains=82) | Q(edad__icontains=87))
        return resultado
    def buscar_autor5(self, kword):
        resultado = self.filter(edad__gt=40, edad__lt=80).order_by('apellidos', 'nombres', 'id')
        return resultado





