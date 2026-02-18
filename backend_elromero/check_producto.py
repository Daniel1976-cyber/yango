from tienda.models import Producto

def check_productos():
    print("Productos en la base de datos:")
    for producto in Producto.objects.all():
        print(f"ID: {producto.pk} | Nombre: {producto.nombre} | Activo: {producto.activo}")

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, '.')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')
    import django
    django.setup()
    check_productos()
