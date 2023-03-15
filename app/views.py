

from django.shortcuts import render



def login(request):
    return render(request, 'login.html')

def cadastro(request):
  return render(request, 'cadastro.html')

def menu (request):
          return render (request, 'menu.html')


def cadastrarcomeia(request):
    return render(request, 'cadastrarcomeia.html')
def header(request):
    return render(request, 'header.html')

