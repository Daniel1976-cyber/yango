import requests
API_BASE = 'http://127.0.0.1:8000/api'

# Obtener MacBook Air
response = requests.get(f'{API_BASE}/productos/2/')
if response.status_code == 200:
    producto = response.json()
    print(f'Producto antes: {producto["nombre"]} - Activo: {producto["active"]}')

    # Activar producto
    data = producto.copy()
    data['activo'] = True
    response = requests.put(f'{API_BASE}/productos/2/', json=data)
    if response.status_code == 200:
        producto = response.json()
        print(f'Producto después: {producto["nombre"]} - Activo: {producto["active"]}')
    else:
        print(f'Error al actualizar: {response.status_code}')
else:
    print(f'Error al obtener producto: {response.status_code}')
