

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClienteForm
from .models import Cliente
def login(request):
    return render(request, 'login.html')

def cadastro(request):

    return render(request, 'cadastro.html')


def menu (request):
          return render (request, 'menu.html')

def cadastrarcomeia(request):
    return render(request, 'cadastrarcomeia.html')
def addcolheita(request):
    return render(request, 'addcolheita.html')

#list_cliente, create_cliente,  update_cliente, delete_cliente


def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def create_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')

    return render(request, 'clientes-form.html', {'form': form})


def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('list_clientes')

    return render(request, 'clientes-form.html', {'form': form, 'cliente': cliente})


def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('list_clientes')

    return render(request, 'clie-delete-confirm.html', {'cliente': cliente})