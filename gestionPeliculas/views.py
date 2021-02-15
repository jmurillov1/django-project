from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template.loader import get_template
import requests

def peliculas(request):

    url="https://api.themoviedb.org/3/movie/now_playing?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=es-ES"

    movies = requests.get(url).json()["results"]

    plantilla = get_template("consulta.html")

    ctx = {"url":url, "nombre":movies}

    documento = plantilla.render(ctx)

    return HttpResponse(documento)

def get_movie(request, codigo):

    url='https://api.themoviedb.org/3/movie/{}?api_key=38b1ff54cd4e1a6336da76eee04c670e&language=en-US'.format(codigo)
    
    movies = requests.get(url).json()

    documento = str(movies)

    return HttpResponse(documento)

def login_page(request):
    
    return HttpResponse("Login")
