from ast import Pass
from operator import index
from django.shortcuts import render
from.models import familia
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def crear (request):
    familiar1= familia( nombre='Pedro', identificacion= 20320485, fecha= '1986-09-12')
    familiar2= familia( nombre='Marie', identificacion= 21320785, fecha= '1991-02-10')
    
    familiar1.save()
    familiar2.save()
    
    return HttpResponse('Creado con exito')

def mostrar(request):
    
    info= familia.objects.all()
    
    dicc={"familiares": info}
    
    index= loader.get_template ('index.html')
    
    documento= index.render(dicc)
    
    return HttpResponse(documento)