from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
 #return HttpResponse("Meu primeiro response html django")
    return render(request, 'login.html')
def cadastro(request):
  return render(request, 'cadastro.html')