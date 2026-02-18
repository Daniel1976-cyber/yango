#!/usr/bin/env python3
"""Script para cambiar la contraseña del usuario admin de forma no interactiva."""

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
        # Obtener usuario admin
        user = User.objects.get(username='admin')
        # Cambiar contraseña (usa la contraseña que desees)
        user.set_password('admin123')
        user.save()
        print("Contraseña del usuario admin actualizada correctamente")
    except User.DoesNotExist:
        print("El usuario admin no existe")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()