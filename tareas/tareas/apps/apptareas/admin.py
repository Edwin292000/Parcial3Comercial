from django.contrib import admin
from .models import tareas
from .models import estado

# Register your models here.

admin.site.register(tareas)

admin.site.register(estado)