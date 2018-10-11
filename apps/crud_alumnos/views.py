# Paso 11. Crear una vista
# Paso 12. Agregar a la carpeta static los archivos css y js del framework
#          materialize
# Paso 13. Crear las carpetas 'base' y 'crudalumnos' en la carpeta templates
# Paso 14. Crear los archivos base.html y alumnos_form.html y guardarlos en
#          las carpetas 'base' y 'crudalumnos' respectivamente

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.crud_alumnos.models import alumnos, carreras
from apps.crud_alumnos.forms import alumnosForm, carrerasForm
from apps.crud_alumnos.filters import alumnosFilter, carrerasFilter
from django.urls import reverse_lazy
# Create your views here.


class alumnosCreate(CreateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnosList(ListView):
    queryset = alumnos.objects.order_by('nocontrol')
    template_name = 'crudalumnos/alumnos_list.html'
    paginate_by = 1


class alumnosUpdate(UpdateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnosDelete(DeleteView):
    model = alumnos
    template_name = 'crudalumnos/alumnos_delete.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnoShow(DetailView):
    model = alumnos
    template_name = 'crudalumnos/alumno_show.html'
# buscar o filtrar
# Para agregar la vista de búsqueda, se instala primero
# pip install django-filters
def search(request):
    alumnos_list = alumnos.objects.all()
    alumnos_filter = alumnosFilter(request.GET, queryset=alumnos_list)
    return render(request, 'crudalumnos/alumnos_list_filter.html', {'filter': alumnos_filter})
#aqui inicia el crud de carrreras

class carrerasCreate(CreateView):
    model = carreras
    form_class = carrerasForm
    template_name = 'crudalumnos/carreras_form.html'
    success_url = reverse_lazy ('carreras:carrera_lista')


class carrrerasList(ListView):
    queryset = carreras.objects.order_by('id')
    template_name = 'crudalumnos/carreras_list.html'
    paginate_by = 10


class carrerasUpdate(UpdateView):
    model = carreras
    form_class = carrerasForm
    template_name = 'crudalumnos/carreras_form.html'
    success_url = reverse_lazy('carreras:carrera_lista')


class carrerasDelete(DeleteView):
    model = carreras
    template_name = 'crudalumnos/carreras_delete.html'
    success_url = reverse_lazy('carreras:carrera_lista')


class carrerasShow(DetailView):
    model = carreras
    template_name = 'crudalumnos/carrera_show.html'

def search_c(request):
    carreras_list = carreras.objects.all()
    carreras_filter = carrerasFilter(request.GET, queryset=carreras_list)
    return render(request, 'crudalumnos/carreras_list_filter.html', {'filter': carreras_filter})