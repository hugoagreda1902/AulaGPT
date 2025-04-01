# api/models.py
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=100)  # Nombre del usuario
    correo = models.EmailField(unique=True)  # Correo electrónico único
    password = models.CharField(max_length=255)  # Contraseña del usuario

    def __str__(self):
        return self.nombre
