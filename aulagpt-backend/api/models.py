from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, role, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, role='teacher', password=None):
        user = self.create_user(email, name, surname, role, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'role']

    objects = UserManager()

    def __str__(self):
        return f"{self.name} {self.surname} ({self.role})"

    
class UserClass (models.Model):
    # Modelo intermedio para relacionar usuarios y clases
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)      # FK a User
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)    # FK a Class

    class Meta:
        unique_together = ('user_id', 'class_id')                       # No permitir duplacados en la relación
    
    def __str__(self):
        return f"{self.user} in {self.class_id}"
    
class Class (models.Model):
    class_id = models.AutoField(primary_key=True)                 # ID autoincremental como PK 
    class_name = models.CharField(max_length=100)                 # Nombre descriptivo de la clase
    acces_code = models.CharField(max_length=20, unique=True)     # Código para unirse a la clase (único)
    
    users = models.ManyToManyField(User, through=UserClass)       # Relación ManyToMany con usuarios, usando tabla intermedia UserClass

    def __str__(self):
        return self.class_name
    
class Documents (models.Model):
    document_id = models.AutoField (primary_key=True)                                            # ID autoincremental del documento
    class_id = models.ForeignKey (Class, on_delete=models.CASCADE, related_name='documents')     # FK a la clase a la que pertenece
    file_name = models.CharField (max_length=200)                                                # Nombre del archivo
    file_type = models.CharField (max_length=10)                                                 # Tipo de archivo (PDF, DOCX...)
    upload_date = models.DateTimeField (auto_now_add=True)                                       # Fecha automática de subida
    drive_link = models.URLField ()                                                              # URL del archivo en Google Drive

    def __str__(self):
        return self.file_name

class Tests (models.Model):
    test_id = models.AutoField (primary_key=True)                                                # No permitir duplacados en la relación
    user_id = models.ForeignKey (User, on_delete=models.CASCADE, related_name='tests_created')   # FK al alumno creador del test
    document_id = models.ForeignKey (Documents, on_delete=models.CASCADE, related_name='tests')  # FK al codumento usado para el test
    test_name = models.CharField (max_length=200)                                                # Nombre del test                                        
    creation_date = models.DateTimeField (auto_now_add=True)                                     # Fecha de creación automática

    def __str__(self):
        return self.test_name
    
class TestQuestion (models.Model):
    question_id = models.AutoField (primary_key=True)                                              # ID de la pregunta
    test_id = models.ForeignKey (Tests, on_delete=models.CASCADE, related_name='questions')        # FK al test
    question_text = models.TextField ()                      # Texto de la pregunta 
    option_1 = models.CharField (max_length=200)             # Opción 1
    option_2 = models.CharField (max_length=200)             # Opción 2
    option_3 = models.CharField (max_length=200)             # Opción 3
    correct_option = models.CharField (max_length=10)        # Opción correcta

    def __str__(self):
        return self.question_text[:50]                       # Muestra los primeros 50 caracteres

class TestAnswer (models.Model):
    answer_id = models.AutoField(primary_key=True)                                                 # ID de la respuesta
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')               # FK al usuario que responde
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='answers')              # FK al test contestado
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='answers')   # FK a la pregunta respondida
    selected_option = models.CharField(max_length=10)                                              # Opción elegida por el alumno
    is_correct = models.BooleanField()                                                             # Si la respuesta es correcta o no
    answer_date = models.DateTimeField(auto_now_add=True)                                          # Fecha y hora de la respuesta

    def __str__(self):
        return f"Answer by {self.user} on {self.answer_date}"
    
class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)                                              # ID del registro de actividad
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')            # FK al usuario
    ACTIVITY_TYPES = (
        ('upload', 'Upload'),
        ('test', 'Test'),
        ('answer', 'Answer'),
    )
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_TYPES)                        # Tipo de actividad
    timestamp = models.DateTimeField(auto_now_add=True)                                            # Fecha y hora de la actividad

    def __str__(self):
        return f"{self.activity_type} by {self.user} at {self.timestamp}"