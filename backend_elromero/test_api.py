import requests
import json

API_BASE = 'http://127.0.0.1:8000/api'

def test_productos_activos():
    print("Test: Obtener productos activos")
    response = requests.get(f'{API_BASE}/productos/')
    if response.status_code == 200:
        productos = response.json()
        print(f'Total productos: {len(productos)}')
        for producto in productos:
            print(f'{producto["nombre"]} - Activo: {producto["active"]}')
    else:
        print(f'Error: {response.status_code}')

def test_productos_inactivos():
    print("\nTest: Obtener productos inactivos")
    response = requests.get(f'{API_BASE}/productos/?activo=False')
    if response.status_code == 200:
        productos = response.json()
        print(f'Total productos inactivos: {len(productos)}')
        for producto in productos:
            print(f'{producto["nombre"]} - Activo: {producto["active"]}')
    else:
        print(f'Error: {response.status_code}')

def test_cambiar_estado_producto(id, activo):
    print(f"\nTest: Cambiar estado del producto {id} a {activo}")
    # Primero ver el producto
    response = requests.get(f'{API_BASE}/productos/{id}/')
    if response.status_code == 200:
        producto = response.json()
        print(f'Producto antes: {producto["nombre"]} - Activo: {producto["active"]}')
        
        # Cambiar estado
        data = producto.copy()
        data['activo'] = activo
        response = requests.put(f'{API_BASE}/productos/{id}/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            producto = response.json()
            print(f'Producto después: {producto["nombre"]} - Activo: {producto["active"]}')
        else:
            print(f'Error al actualizar: {response.status_code}')
    else:
        print(f'Error al obtener producto: {response.status_code}')

# Pruebas
test_productos_activos()
test_productos_inactivos()

# Si hay productos, probar a cambiar su estado
response = requests.get(f'{API_BASE}/productos/')
if response.status_code == 200:
    productos = response.json()
    if productos:
        # Cambiar el estado del primer producto
        id_producto = productos[0]['id']
        nuevo_estado = not productos[0]['active']
        test_cambiar_estado_producto(id_producto, nuevo_estado)
