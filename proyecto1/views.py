from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from app1.models import *
from random import randint

def bienvenida(request):
    return HttpResponse ("Bienvenidos al curso, lacras")

def bienvenida_html (request):
    hoy=datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2> La experiencia es la madre de todas las ciencias </h2>
    <h3> hoy estamos a {hoy}</h3>
    </html>
    """
    return HttpResponse (response)

def saludar (request, nombre):
    response = f"hola que tal {nombre}, como te encuentras hoy?"
    return HttpResponse (response)

def total_propina (request, total):
    total= float(total)
    response= f"<html><h1>el total de la compra con la propina incluida es USD {round(total*1.1, 2)}</h1></html>"
    return HttpResponse(response)

def saludar2 (request, nombre, apellido):
    response = f"<html><h1>hola que tal {nombre} {apellido}, como te encuentras hoy?</h1><html>"
    return HttpResponse (response)


def bienvenida_template(request):
    nombre = "Filia"
    apellido = "Villanera"
    curso = "Python & Django"
    notas= [4,8,7,6,7,6]
    diccionario = {"nombre":nombre, "apellido":apellido, "curso":curso, "notas":notas, "hoy":datetime.datetime.now()}
    
    plantilla= loader.get_template("bienvenido.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)


def comision_1 (request):
    nombre = "Filia"
    apellido = "Villanera"
    curso = "Python & Django"
    notas= [4,8,7,6,7,6]
    diccionario = {"nombre":nombre, "apellido":apellido, "curso":curso, "notas":notas, "hoy":datetime.datetime.now()}
    
    plantilla= loader.get_template("comision_1.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)

def agg_curso(request):
    str_nombre = "python"
    nro_comision = randint(1,99999)
    curso = Curso(nombre=str_nombre , comision= nro_comision)
    curso.save()
    documento= f"<html><h1>Se acaba de crear un curso de {str_nombre} con numero de comision No. {nro_comision}</h1></html>"
    return HttpResponse (documento)