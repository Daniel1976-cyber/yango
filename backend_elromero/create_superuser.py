#!/usr/bin/env python3
"""Script para crear un superusuario admin de forma no interactiva."""

import sys
import django
from django.contrib.auth import get_user_model

# Configurar Django
sys.path.insert(0, '.')
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')
django.setup()

User = get_user_model()

def main():
    try:
        # Verificar si el usuario admin existe
        try:
            user = User.objects.get(username='admin')
            print("El usuario admin ya existe")
        except User.DoesNotExist:
            # Crear nuevo superusuario
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            user.save()
            print("Superusuario admin creado correctamente")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
