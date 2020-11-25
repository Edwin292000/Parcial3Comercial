import graphene

from graphene_django import DjangoObjectType

from .models import *

class tareaType(DjangoObjectType):
    class Meta:
        model=tareas


class estadoType(DjangoObjectType):
    class Meta:
        model=estado


class Query(graphene.ObjectType):
    tareas=graphene.List(tareaType)
    estado=graphene.List(estadoType)

    def resolve_tareas(self, info, **kwargs):
        return tareas.objects.all()

    def resolve_estado(self, info, **kwargs):
        return estado.objects.all()


    
