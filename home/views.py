from django.shortcuts import render

# Create your views here. // Aqui ficam as minhas visualizações
# Pesquisar sobre class bases views

def home(request):
    print('Home')
    return render(
        request,
        'home.html'
    )
