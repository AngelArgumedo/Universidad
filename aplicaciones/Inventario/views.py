from django.shortcuts import render, redirect
from .models import Objeto
# Create your views here.

def home(request):
    objetos = Objeto.objects.all()
    return render(request, "gestionObjetos.html", {"objetos": objetos})

def registrarObjeto(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    cantidad = request.POST["numCantidad"]
    Objeto.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    return redirect('/')

def edicionObjeto(request, codigo):
    objeto = Objeto.objects.get(codigo=codigo)
    return render(request, "edicionObjeto.html", {"objeto": objeto})

def editarObjeto(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    cantidad = request.POST["numCantidad"]
    objeto = Objeto.objects.get(codigo=codigo)
    objeto.nombre = nombre
    objeto.cantidad = cantidad
    objeto.save()
    return redirect('/')

def eliminarObjeto(request, codigo):
    objeto = Objeto.objects.get(codigo=codigo)
    objeto.delete()
    return redirect('/')