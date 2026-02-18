# Bazar El Romero - Proyecto de Tienda Online

## Descripción

Bazar El Romero es una tienda online para la venta de productos de ropa, hogar, plantas y más. El proyecto está desarrollado con Django para el backend y HTML/CSS/JavaScript para el frontend.

## Requisitos previos

- Python 3.x
- Django 6.0.1
- Virtual environment (venv)

## Instalación y configuración

### 1. Clonar el repositorio

### 2. Activar el entorno virtual
```bash
# En Windows
venv_elromero\Scripts\activate

# En macOS/Linux
source venv_elromero/bin/activate
```

### 3. Iniciar el servidor de desarrollo
```bash
cd backend_elromero
python manage.py runserver
```

El servidor se ejecutará en `http://127.0.0.1:8000/`

## URLs importantes

### Frontend
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/` | Tienda pública (vista de clientes) |
| `http://127.0.0.1:8000/nuevo-producto` | Formulario para agregar productos (administración) |

### Backend/API
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/admin/` | Panel de administración de Django |
| `http://127.0.0.1:8000/api/productos/` | API para productos |
| `http://127.0.0.1:8000/api/categorias/` | API para categorías |
| `http://127.0.0.1:8000/api/clientes/` | API para clientes |
| `http://127.0.0.1:8000/api/pedidos/` | API para pedidos |

## Funcionalidades

### Tienda pública (`/`)
- Ver productos por categoría
- Filtrar productos
- Agregar productos al carrito
- Enviar pedido por WhatsApp
- Ver productos disponibles/agotados

### Administración
#### Panel de Django (`/admin/`)
- Gestionar productos
- Gestionar categorías
- Gestionar clientes
- Gestionar pedidos

#### Formulario de agregar productos (`/nuevo-producto`)
- Formulario para agregar productos con imagen
- Visualizar lista de productos
- Marcar productos como activos/agotados

## Estructura del proyecto

```
backend_elromero/
├── tienda/                      # App principal
│   ├── templates/
│   │   └── tienda/
│   │       ├── bazarelromero.html     # Tienda pública
│   │       └── agregar_producto.html  # Formulario de administración
│   ├── views.py                 # Vistas para frontend
│   ├── tienda_views.py          # Vistas de API
│   ├── models.py                # Modelos de datos
│   ├── forms.py                 # Formularios
│   ├── tienda_urls.py           # URLs de API
│   └── tienda_serializers.py    # Serializadores de API
├── media/                       # Archivos multimedia (imagenes de productos)
├── static/                      # Archivos estáticos (CSS, JS, imágenes)
├── backend_elromero/            # Configuración del proyecto
│   ├── settings.py              # Configuraciones
│   └── urls.py                  # URLs principales
└── db.sqlite3                   # Base de datos SQLite
```

## Uso básico

### Para clientes
1. Acceder a `http://127.0.0.1:8000/`
2. Navegar por las categorías
3. Hacer clic en "Agregar" para agregar productos al carrito
4. Ver el carrito haciendo clic en el ícono de compras
5. Enviar el pedido por WhatsApp

### Para administradores
1. Acceder a `http://127.0.0.1:8000/admin/` (se necesita usuario y contraseña)
2. O acceder a `http://127.0.0.1:8000/nuevo-producto` para agregar productos directamente
3. Rellenar el formulario con los datos del producto y la imagen
4. Hacer clic en "Guardar"

## Configuración adicional

### Crear usuario admin
```bash
python manage.py createsuperuser
```

### Recolectar archivos estáticos
```bash
python manage.py collectstatic
```

### Migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

## Tecnologías usadas

- **Backend**: Django 6.0.1
- **API**: Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Base de datos**: SQLite
- **Herramientas**: Bootstrap (para estilos), jQuery (para interacción)

## Notas importantes

- El proyecto está en modo DEBUG=True para desarrollo
- Las imágenes de productos se guardan en la carpeta `media/productos/`
- Los archivos estáticos se guardan en la carpeta `static/imagenes/`
- La tienda usa localStorage para guardar el catálogo en caso de fallo de conexión
