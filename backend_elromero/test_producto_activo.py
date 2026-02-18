from tienda.models import Producto, Categoria

# Configurar Django
import os
import sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_elromero.settings')
import django
django.setup()

def test_crear_producto_activo():
    print("Test 1: Crear productos de prueba")
    # Verificar si existe una categoría
    if not Categoria.objects.exists():
        categoria = Categoria.objects.create(nombre='Test Categoría', descripcion='Categoría de prueba')
        print(f"Created category: {categoria}")
    else:
        categoria = Categoria.objects.first()
        print(f"Using existing category: {categoria}")
    
    # Crear producto activo
    producto_activo = Producto.objects.create(
        categoria=categoria,
        nombre='Producto Activo',
        descripcion='Este producto está activo',
        precio=19.99,
        stock=10,
        activo=True
    )
    print(f"Created active product: {producto_activo}")
    
    # Crear producto inactivo
    producto_inactivo = Producto.objects.create(
        categoria=categoria,
        nombre='Producto Inactivo',
        descripcion='Este producto está inactivo',
        precio=29.99,
        stock=5,
        activo=False
    )
    print(f"Created inactive product: {producto_inactivo}")
    
    return producto_activo, producto_inactivo

def test_consultar_productos_activos():
    print("\nTest 2: Consultar productos activos")
    productos_activos = Producto.objects.filter(activo=True)
    print(f"Total active products: {productos_activos.count()}")
    for p in productos_activos:
        print(f"- {p.nombre} (Activo: {p.activo})")
    
    print("\nTest 3: Consultar productos inactivos")
    productos_inactivos = Producto.objects.filter(activo=False)
    print(f"Total inactive products: {productos_inactivos.count()}")
    for p in productos_inactivos:
        print(f"- {p.nombre} (Activo: {p.activo})")

def test_cambiar_estado_producto(producto):
    print(f"\nTest 4: Cambiar estado de producto {producto.nombre}")
    nuevo_estado = not producto.activo
    producto.activo = nuevo_estado
    producto.save()
    print(f"Estado cambiado a: {nuevo_estado}")
    producto.refresh_from_db()
    assert producto.activo == nuevo_estado
    print("✓ Estado actualizado correctamente")

if __name__ == "__main__":
    print("Testing Producto Activo functionality")
    print("=" * 30)
    
    # Crear productos
    try:
        prod_activo, prod_inactivo = test_crear_producto_activo()
        
        # Test consultas
        test_consultar_productos_activos()
        
        # Test cambiar estado
        test_cambiar_estado_producto(prod_activo)
        
        print("\n" + "=" * 30)
        print("All tests passed!")
        
    except Exception as e:
        print(f"Error: {e}")
