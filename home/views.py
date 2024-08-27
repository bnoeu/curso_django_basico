from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. // Aqui ficam as minhas visualizações
# Pesquisar sobre class bases views

def home(request):
    print('Home')
    return HttpResponse('home')
