# aula_gpt_backend/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a AulaGPT")
