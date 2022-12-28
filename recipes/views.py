from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Danilo Frazão'
    })


def contato(request):
    return render(request, 'me_apague/temp.html')


def sobre(request):
    return HttpResponse('SOBRE')
