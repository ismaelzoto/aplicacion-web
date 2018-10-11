from django.conf.urls import url
from apps.crud_alumnos.views import alumnosCreate, alumnosList, alumnosDelete, alumnosUpdate, alumnoShow, search, \
    carrerasCreate, carrrerasList, carrerasUpdate, carrerasDelete, carrerasShow, search_c

urlpatterns = [
    url(r'^nuevo/', alumnosCreate.as_view(), name='alumno_crear'),
    url(r'^listar/', alumnosList.as_view(), name='alumnos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', alumnosDelete.as_view(), name='alumno_eliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', alumnosUpdate.as_view(), name='alumno_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', alumnoShow.as_view(), name='alumno_mostrar'),
    url(r'^buscar/$', search, name='alumno_buscar'),
    #aqui inicia el crud de carreras
    url(r'^nueva/', carrerasCreate.as_view(), name='carrera_crea'),
    url(r'^lista/', carrrerasList.as_view(), name='carrera_lista'),
    url(r'^edita/(?P<pk>\d+)/$', carrerasUpdate.as_view(), name='carrera_edita'),
    url(r'^borrar/(?P<pk>\d+)/$', carrerasDelete.as_view(), name='carrera_borrar'),
    url(r'^ver/(?P<pk>\d+)/$', carrerasShow.as_view(), name='carrera_ver'),
    url(r'^busca/$', search_c, name='carrera_busca')
]
