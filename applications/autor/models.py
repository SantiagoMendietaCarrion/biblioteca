from django.db import models

#managers
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos

class Autor(Persona):
    seudonimo = models.CharField('seudonimo', max_length=50, blank=True)
    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
