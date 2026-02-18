import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')
django.setup()

from tienda.models import Categoria, Producto, Cliente, Pedido, DetallePedido

def populate_db():
    print("Populando base de datos con datos de prueba...")
    
    # Categorías
    categoria1 = Categoria.objects.create(nombre="Electrónica", descripcion="Productos electrónicos")
    categoria2 = Categoria.objects.create(nombre="Ropa", descripcion="Ropa y accesorios")
    categoria3 = Categoria.objects.create(nombre="Hogar", descripcion="Productos para el hogar")
    
    # Productos
    producto1 = Producto.objects.create(
        categoria=categoria1,
        nombre="iPhone 15",
        descripcion="Teléfono inteligente Apple",
        precio=999.99,
        stock=50
    )
    
    producto2 = Producto.objects.create(
        categoria=categoria1,
        nombre="MacBook Air",
        descripcion="Laptop Apple",
        precio=1199.99,
        stock=25
    )
    
    producto3 = Producto.objects.create(
        categoria=categoria2,
        nombre="Camiseta",
        descripcion="Camiseta de algodón",
        precio=19.99,
        stock=100
    )
    
    producto4 = Producto.objects.create(
        categoria=categoria3,
        nombre="Lámpara",
        descripcion="Lámpara de escritorio",
        precio=29.99,
        stock=75
    )
    
    # Clientes
    cliente1 = Cliente.objects.create(
        nombre="Juan Pérez",
        email="juan@example.com",
        telefono="1234567890",
        direccion="Calle Principal 123"
    )
    
    cliente2 = Cliente.objects.create(
        nombre="María García",
        email="maria@example.com",
        telefono="0987654321",
        direccion="Avenida Secundaria 456"
    )
    
    # Pedidos
    pedido1 = Pedido.objects.create(
        cliente=cliente1,
        estado="completado",
        total=1019.98
    )
    
    pedido2 = Pedido.objects.create(
        cliente=cliente2,
        estado="procesando",
        total=49.98
    )
    
    # Detalles de Pedido
    DetallePedido.objects.create(
        pedido=pedido1,
        producto=producto1,
        cantidad=1,
        precio_unitario=999.99
    )
    
    DetallePedido.objects.create(
        pedido=pedido1,
        producto=producto3,
        cantidad=1,
        precio_unitario=19.99
    )
    
    DetallePedido.objects.create(
        pedido=pedido2,
        producto=producto3,
        cantidad=2,
        precio_unitario=19.99
    )
    
    DetallePedido.objects.create(
        pedido=pedido2,
        producto=producto4,
        cantidad=1,
        precio_unitario=29.99
    )
    
    print("Base de datos poblada con éxito!")
    print(f"Categoria: {Categoria.objects.count()}")
    print(f"Productos: {Producto.objects.count()}")
    print(f"Clientes: {Cliente.objects.count()}")
    print(f"Pedidos: {Pedido.objects.count()}")
    print(f"Detalles de Pedido: {DetallePedido.objects.count()}")

if __name__ == "__main__":
    populate_db()
