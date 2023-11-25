from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def view_inicio(xx):
    return render(xx, "AppCoder/padre.html")

# def view_cursos(xx):
#     return render(xx, "AppCoder/padre.html")

def view_cursos(xx):
    nombre = "nicolas ezequiel"
    apellido = "palacios"
    diccionario = {'nombre': nombre, 'apellido': apellido}

    ruta = r"C:\Users\Nico\Desktop\proyecto_final_47790\Proyecto_02\AppCoder\templates\AppCoder\padre.html"
    mi_archivo = open(ruta, "r") 

    plantilla = Template(mi_archivo.read())
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    
    return httpresonse(documento)
