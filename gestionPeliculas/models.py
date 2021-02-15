from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.CharField(max_lenght=10)
    nombre = models.CharField(max_lenght=30)
    apellido = models.CharField(max_lenght=30)
    correo = models.EmailField(max_lenght=30)
    nombre = models.CharField(max_lenght=10)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)