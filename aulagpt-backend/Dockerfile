# Usamos una imagen base que tenga Python
FROM python:3.10-slim

# Instalamos las dependencias del sistema necesarias para mysqlclient y las herramientas de compilación
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    gcc \
    && apt-get clean

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de tu proyecto
COPY . .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt
