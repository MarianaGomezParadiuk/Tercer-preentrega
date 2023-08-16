from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request, 'appBiblioteca/home.html')

def db(request):
    contexto = {'lector': Lector.objects.all(),'pedido':Pedido.objects.all(),'bibliotecario': Bibliotecario.objects.all(),'libros': Libro.objects.all()}
    return render(request, 'appBiblioteca/db.html',contexto)

def registroForm(request):
    if request.method == "POST":
        miForm = LectorForm(request.POST)
        if miForm.is_valid():
            lector_nombre = miForm.cleaned_data.get('nombre')
            lector_apellido = miForm.cleaned_data.get('apellido')
            lector_direccion = miForm.cleaned_data.get('direccion')
            lector_email = miForm.cleaned_data.get('email')
            lector_telefono = miForm.cleaned_data.get('telefono')
            lector = Lector(nombre = lector_nombre,
                            apellido = lector_apellido,
                            direccion = lector_direccion,
                            email = lector_email,
                            telefono = lector_telefono)
            lector.save()
            return render(request, 'appBiblioteca/db.html')
    else:
        miForm = LectorForm()

    return render(request,'appBiblioteca/registroForm.html',{"form": miForm })

def pedidoForm(request):
    if request.method == "POST":
        miForm = PedidoForm(request.POST)
        if miForm.is_valid():
            pedido_titulo = miForm.cleaned_data.get('titulo')
            pedido_id_lector = miForm.cleaned_data.get('id_lector')
            pedido = Pedido(titulo = pedido_titulo,
                            id_lector = pedido_id_lector)
            pedido.save()
            return render(request, 'appBiblioteca/db.html')
    else:
        miForm = PedidoForm()
    return render(request,'appBiblioteca/pedidoForm.html',{"form": miForm })

def aplicanteForm(request):
    if request.method == "POST":
        miForm = BibliotecarioForm(request.POST)
        if miForm.is_valid():
            aplicante_nombre = miForm.cleaned_data.get('nombre')
            aplicante_apellido = miForm.cleaned_data.get('apellido')
            aplicante_contacto = miForm.cleaned_data.get('contacto')
            aplicante = Bibliotecario(nombre = aplicante_nombre,
                                      apellido = aplicante_apellido, 
                                      contacto = aplicante_contacto)
            aplicante.save()
            return render(request, 'appBiblioteca/db.html')
    else:
        miForm = BibliotecarioForm()

    return render(request,'appBiblioteca/aplicanteForm.html',{"form": miForm })

def libroForm(request):
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro_titulo = miForm.cleaned_data.get('titulo')
            libro_tipo = miForm.cleaned_data.get('tipo')
            libro_autor = miForm.cleaned_data.get('autor')
            libro_editorial = miForm.cleaned_data.get('editorial')
            libro_cantidad = miForm.cleaned_data.get('cantidad')
            libro = Libro(titulo = libro_titulo,
                          tipo = libro_tipo,
                          autor = libro_autor,
                          editorial = libro_editorial,
                          cantidad = libro_cantidad)
            libro.save()
            return render(request, 'appBiblioteca/db.html')
    else:
        miForm = LibroForm()

    return render(request,'appBiblioteca/libroForm.html',{"form": miForm })

def buscarLibro(request):
    return render(request, 'appBiblioteca/buscarLibro.html')

def buscar(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        libros = Libro.objects.filter(titulo__icontains=patron)
        contexto ={'libros':libros,'titulo':f'Libros que tienen como patron "{patron}"'}
        return render(request,'appBiblioteca/db.html',contexto)
    return HttpResponse('No se ingreso nada a buscar')
