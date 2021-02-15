from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template.loader import get_template
import requests
from django.views.decorators.csrf import csrf_exempt
from gestionPeliculas.models import Cliente
from django.core import serializers
from django.http import JsonResponse


def peliculas(request):

    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=es-ES"

    movies = requests.get(url).json()["results"]

    ctx = {"nombre": movies}

    return render(request, "listado.html", ctx)


def get_movie(request, codigo):

    url = 'https://api.themoviedb.org/3/movie/{}?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=es-ES'.format(
        codigo)

    movie= {"movie":requests.get(url).json()}

    return render(request, "moviedetail.html", movie)

def get_reserva(request, codigo):

    url = 'https://api.themoviedb.org/3/movie/{}?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=es-ES'.format(
        codigo)

    movie= {"movie":requests.get(url).json()}

    return render(request, "detallereserva.html", movie)

def login_page(request):
    return render(request, "login.html")


@csrf_exempt
def ingresar(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    cliente = Cliente.validar_login(username, password)
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=es-ES"
    movies = requests.get(url).json()["results"]
    ctx = {"cliente": cliente, "nombre": movies}
    if cliente:
        request.session['cliente'] = serializers.serialize('json', [cliente, ])[0]
        return render(request, "listado.html", ctx)
    else:
        return render(request, "login.html")


def cuenta(request):
    print(request.session['cliente'])
    if "cliente" in request.session:
        result = request.session.get("cliente")
    else:
        result = False
    print(result)
    ctx = {"cliente": result}
    return render(request, "account.html", ctx)

def get_movie_id(request, codigo):
    return JsonResponse({"id": codigo})