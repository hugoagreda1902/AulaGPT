# utils.py

from googleapiclient.discovery import build
from google.oauth2 import service_account

# Cambia esto por la ruta a tu archivo de credenciales
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    return service

def create_drive_folder(folder_name, parent_folder_id=None):
    service = get_drive_service()
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
    }
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]

    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')
