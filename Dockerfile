# Dockerfile
FROM python:3.11-slim

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
