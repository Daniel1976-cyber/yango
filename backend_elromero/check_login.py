from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

# Configurar Django
import os
import sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')
import django
django.setup()

User = get_user_model()

def check_login():
    # Verificar si el usuario existe
    try:
        user = User.objects.get(username='admin')
        print('Usuario admin existe')
        
        # Intentar autenticar
        authenticated_user = authenticate(username='admin', password='admin123')
        if authenticated_user is not None:
            print('Login exitoso')
            print(f'User ID: {authenticated_user.id}')
            print(f'Is Superuser: {authenticated_user.is_superuser}')
        else:
            print('Login fallido')
            
    except User.DoesNotExist:
        print('El usuario admin no existe')

if __name__ == "__main__":
    check_login()
