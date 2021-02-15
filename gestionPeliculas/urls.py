"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestionPeliculas import views as vw

urlpatterns = [
    path('login/',vw.login_page, name="Login"),
    path('',vw.peliculas, name="Inicio"),
    path('movie/<int:codigo>',vw.get_movie, name="Pelicula"),
    path('detalle/<int:codigo>',vw.get_reserva, name="Reserva"),
    path('',vw.ingresar, name="Validar"),
    path('account/',vw.cuenta, name="Cuenta"),
    path('moviejson/<int:codigo>',vw.get_movie_id, name="Json"),
]