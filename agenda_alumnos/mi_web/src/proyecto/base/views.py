from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Alumno


class Logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy ('alumnos')

class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('alumnos')

    def form_valid(self, form):
        usuario=form.save()
        if usuario is not None:
            login(self.request,usuario)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('alumnos')
        return super(PaginaRegistro, self).get(*args, **kwargs)

class ListaAlumnos(LoginRequiredMixin,ListView):
    model= Alumno
    context_object_name = 'alumnos'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['alumnos'] = context['alumnos'].filter(usuario=self.request.user)
        context['count'] = context['alumnos'].filter(completo=False).count()
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['alumnos'] = context['alumnos'].filter(nombre__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

class DetalleAlumnos(LoginRequiredMixin,DetailView):
    model = Alumno
    context_object_name = 'alumno'
    template_name = 'base/alumno.html'


class CrearAlumnos(LoginRequiredMixin,CreateView):
    model = Alumno
    fields= ['nombre','apellido','completo']
    success_url=reverse_lazy('alumnos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearAlumnos, self).form_valid(form)


class EditarAlumnos(LoginRequiredMixin,UpdateView):
    model = Alumno
    fields = ['nombre','apellido','completo']
    success_url = reverse_lazy('alumnos')

class EliminarAlumnos(LoginRequiredMixin,DeleteView):
    model = Alumno
    fields = 'alumno'
    success_url = reverse_lazy('alumnos')
