from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Prestamo
from .forms import PrestamoForm, MultiplePrestamoForm


class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        # Primera forma para crear un registro en una tabla o modelo
        #Prestamo.objects.create(
        #    lector = form.cleaned_data['lector'],
        #    libro = form.cleaned_data['libro'],
        #    fecha_prestamo=date.today(),
        #    devuelto=False
        #)

        # Segunda forma para crear un registro en una tabla o modelo
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        # Si está en models, ya no colocar aqui
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)

class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        obj, created = Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            defaults={'fecha_prestamo':date.today()}
        )
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect(reverse('lector:error'))

class ErrorView(TemplateView):
    template_name = 'lector/error.html'

class AddMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):
        #
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])
        #
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo=date.today(),
                devuelto=False
            )
            l.stock = l.stock - 1
            l.save()
            prestamos.append(prestamo)
        Prestamo.objects.bulk_create(prestamos)

        return super(AddMultiplePrestamo, self).form_valid(form)


