from django.db import models

# Create your models here.


class carreras(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

# aqui se crea el metodo __str__ para mostrar las carreras en el formulario de alumnos

    def __str__(self):
        return '{}'.format(self.nombre)


class alumnos(models.Model):
    nocontrol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    carreras = models.ForeignKey(carreras, null=True, blank=True, on_delete=models.CASCADE)

"""
despues se ejecuta el comando para realizar la migración del modelo a la base de datos

 python manage.py makemigrations
 python manage.py migrate

se insertan datos a la base de datos con python manage.py shell

 from apps.crud_alumnos.models import carreras

 c = carreras(id = 1, nombre = 'ingenieria en informatica')
 c.save()
"""