from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre_usuario, password=None, **extra_fields):
        """
        Crea y guarda un usuario con un correo y contraseña.
        """
        if not correo:
            raise ValueError('El correo es obligatorio')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, nombre_usuario=nombre_usuario, **extra_fields)  # Aceptar extra_fields
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre_usuario, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con correo, nombre de usuario y contraseña.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Verifica si los campos adicionales están configurados correctamente
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        return self.create_user(correo, nombre_usuario, password, **extra_fields)

    
class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True, db_column='correo')  # Renombrado en DB
    usuario = models.CharField(max_length=150, unique=True, db_column='usuario')  # Renombrado en DB
    nombre = models.CharField(max_length=30, default='Null', db_column='nombre')  # Renombrado en DB
    apellido = models.CharField(max_length=30, default='Null', db_column='apellido')  # Renombrado en DB
    activo = models.BooleanField(default=True, db_column='activo')  # Renombrado en DB
    es_staff = models.BooleanField(default=False, db_column='es_staff')  # Renombrado en DB

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'  # Modificado para usar 'correo' como campo principal de inicio de sesión
    REQUIRED_FIELDS = ['nombre_usuario', 'nombre', 'apellido']

    def __str__(self):
        return self.correo
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=150, unique=True)
    primer_nombre = models.CharField(max_length=30, default='Null')
    apellido = models.CharField(max_length=30, default='Null')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Otros campos y configuraciones
    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['usuario', 'nombre', 'apellido']

    def __str__(self):
        return self.correo
