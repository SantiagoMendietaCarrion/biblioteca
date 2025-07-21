from django.db import models

# Create your models here.
class Persona(models.Model):
    full_name = models.CharField('nombres', max_length=50, blank=True)
    pais = models.CharField('Pais', max_length=30, blank=True)
    pasaporte = models.CharField('Pasaporte', max_length=50, blank=True)
    edad = models.IntegerField(blank=True, null=True)
    apelativo = models.CharField('Apelativo', max_length=10, blank=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais', 'apelativo']
        abstract = True

    def __str__(self):
        return self.full_name

class Empleado (Persona):
    empleo = models.CharField('Empleo', max_length=50, blank=True)

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(edad__gte=18), name='empleado_edad_mayor_18')]

class Cliente (Persona):
    email = models.EmailField('Email', max_length=50, blank=True)

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(edad__gte=18), name='cliente_edad_mayor_18')]

