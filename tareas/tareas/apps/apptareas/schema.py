import graphene

from graphene_django import DjangoObjectType

from .models import *

class tareaType(DjangoObjectType):
    class Meta:
        model=tareas


class estadoType(DjangoObjectType):
    class Meta:
        model=estado

class estadoInput(graphene.InputObjectType):
    nombre=graphene.String()
    descripcion=graphene.String()


class Query(graphene.ObjectType):
    tareas=graphene.List(tareaType)
    estado=graphene.List(estadoType)

    def resolve_tareas(self, info, **kwargs):
        return tareas.objects.all()

    def resolve_estado(self, info, **kwargs):
        return estado.objects.all()


class createEstado(graphene.Mutation):
    id = graphene.Int()
    nombre=graphene.String()
    descripcion=graphene.String()


    class Arguments:
        nombre=graphene.String()
        descripcion=graphene.String()

    def mutate(self, info, nombre, descripcion):
        e=estado(nombre=nombre, descripcion=descripcion)
        e.save()


        return createEstado(
            id=e.id,
            nombre=e.nombre,
            descripcion=e.descripcion
        )
 

class Mutation(graphene.ObjectType):
    create_estado=createEstado.Field()



    
