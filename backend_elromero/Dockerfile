# Dockerfile para el proyecto Django El Romero

FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 👇 Copiar requirements desde la carpeta correcta
COPY backend_elromero/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 👇 Copiar todo el backend correctamente
COPY backend_elromero/ .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend_elromero.wsgi:application"]
