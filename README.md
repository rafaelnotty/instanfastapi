# mydocker2
install fastapi and run web chat app
modify CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] for more efficiency cpu
and deactivate or delete:  volumes:
      - .:/app  # Monta el directorio actual en /app dentro del contenedor

