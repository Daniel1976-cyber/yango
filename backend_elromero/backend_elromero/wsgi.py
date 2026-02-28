"""
WSGI config for backend_elromero project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')

application = get_wsgi_application()

# Automatic migrations on startup (Temporarily disabled for debugging)
# try:
#     print("Running automatic migrations...")
#     call_command('migrate', interactive=False)
#     print("Migrations completed successfully.")
# except Exception as e:
#     print(f"Error running migrations: {e}")

# Add for Vercel
app = application
