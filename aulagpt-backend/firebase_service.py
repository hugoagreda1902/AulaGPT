# firebase-service.py
import firebase_admin
from firebase_admin import credentials, auth

# Configuración de Firebase (asegúrate de tener el archivo JSON de las credenciales)
cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred)

# Funciones de Firebase para interactuar con la base de datos, autenticación, etc.

def get_user_by_email(correo):
    try:
        user = auth.get_user_by_email(correo)
        return user
    except firebase_admin.auth.UserNotFoundError:
        return None
