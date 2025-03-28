FROM python:3.10

WORKDIR /app

# Copia el archivo requirements.txt
COPY requirements.txt /app/requirements.txt

# Copia el resto de los archivos del proyecto
COPY . /app

# Instala las dependencias desde el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la app (ajusta esto según cómo inicies tu app)
CMD ["python", "manage.py", "runserver"]