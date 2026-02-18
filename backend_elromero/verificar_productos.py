import requests
API_BASE = 'http://127.0.0.1:8000/api'

# Obtener productos activos
response = requests.get(f'{API_BASE}/productos/')
if response.status_code == 200:
    productos = response.json()
    print("Productos activos:")
    for producto in productos:
        print(f'{producto["nombre"]} - Activo: {producto["active"]}')
else:
    print(f'Error al obtener productos: {response.status_code}')
