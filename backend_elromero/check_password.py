import django
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()
u = User.objects.get(username='admin')
print('Usuario:', u.username)
print('Contraseña válida:', u.check_password('admin123'))