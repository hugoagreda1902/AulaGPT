from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=255, unique=True)
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.usuario
