from django.db import models
from django.utils import timezone

# Create your models here.

class estado(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()


class tareas(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion = models.TextField()
    estado=models.ForeignKey(estado, on_delete=models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)






    