# aqui se Crea el formulario

from django import forms
from apps.crud_alumnos.models import alumnos, carreras


class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = [
            'nocontrol',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'carreras'
        ]
        labels = {
            'nocontrol': 'Numero de Control',
            'nombre' : 'Nombres',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'carreras': 'Carrera'
        }

        widgets = {
            'nocontrol': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'datepicker'}),
            'carreras': forms.Select(attrs={'class':'form-control'}),
        }


class carrerasForm(forms.ModelForm):
    class Meta:
        model = carreras
        fields = [
            'id',
            'nombre'
        ]
        labels = {
            'id':'Clave de Carrera',
            'nombre':'Nombre de la Carrera'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }