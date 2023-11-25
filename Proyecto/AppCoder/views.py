from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_inicio(xx):
    return HttpResponse( "BIENVENIDOS")

def view_cursos(xx):
    return render(xx, "AppCoder/padre.html")


