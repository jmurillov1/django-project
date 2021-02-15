from django.db import models
from django.db.models import Q # new

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=10)
    numero_cuenta = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def validar_login(self, username="", password=""):
        result = Cliente.objects.filter(Q(username__icontains=username) & Q(password__icontains=password))
        if result:
            return result[0]
        else:
            return False

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()