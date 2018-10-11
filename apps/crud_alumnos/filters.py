import django_filters
from apps.crud_alumnos.models import alumnos, carreras


class alumnosFilter(django_filters.FilterSet):
    class Meta:
        model = alumnos
        fields = ['nocontrol', 'nombre', 'carreras']

class carrerasFilter(django_filters.FilterSet):
    class Meta:
        model = carreras
        fields = ['nombre']
