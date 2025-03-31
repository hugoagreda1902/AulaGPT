# Usa una imagen oficial de Python como base
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt a /app dentro del contenedor
COPY requirements.txt /app/requirements.txt

# Instala las dependencias necesarias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto a /app dentro del contenedor
COPY . /app/

# Exponer el puerto 8000, que es el que usará el backend
EXPOSE 8000

# Comando para iniciar el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]
