# Guía de Despliegue para Bazar El Romero

Esta guía explica cómo deployar la tienda online para que sea accesible desde internet y fácil de usar.

## Requisitos
- Cuenta en GitHub (gratuita)
- Cuenta en Render.com (gratuita)
- Cuenta en Vercel.com (gratuita)

## Paso 1: Subir el código a GitHub
1. Crea un repositorio GitHub (puedes nombrarlo `bazar-el-romero`)
2. Sube todos los archivos del proyecto (carpeta `backend_elromero`)
3. Asegúrate de que el archivo `.gitignore` esté incluido

## Paso 2: Deployar el Backend (Render)
1. Abre [Render.com](https://render.com/) y entra con tu cuenta GitHub
2. Haz clic en **New** > **Web Service**
3. Conecta tu repositorio GitHub (`bazar-el-romero`)
4. Configura:
   - **Name**: bazar-el-romero-api
   - **Region**: Frankfurt (o la más cercana a Cuba)
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backend_elromero.wsgi:application`
5. Haz clic en **Advanced** y agrega variables de entorno:
   - `SECRET_KEY`: Copia tu clave secreta de Django (en `settings.py`)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Tu dominio de Render (ej: `bazar-el-romero-api.onrender.com`)
6. Haz clic en **Deploy** y espera a que termine el proceso

## Paso 3: Crear la Base de Datos (Render)
1. En Render, haz clic en **New** > **PostgreSQL**
2. Configura:
   - **Name**: bazar-el-romero-db
   - **Region**: Mismo que el backend
3. Haz clic en **Create Database**
4. Copia la URL de conexión (starts with `postgres://`)
5. En tu Web Service de Render:
   - Edita las variables de entorno
   - Agrega una variable `DATABASE_URL` con la URL de la base de datos
6. Haz clic en **Save Changes** y espera a que el backend se reinicie

## Paso 4: Migrar la Base de Datos
1. En Render, ve a tu Web Service > **Shell**
2. Ejecuta los comandos:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Ingresa un usuario y contraseña (para el admin)

## Paso 5: Deployar el Frontend (Vercel)
1. Abre [Vercel.com](https://vercel.com/) y entra con tu cuenta GitHub
2. Importa tu repositorio `bazar-el-romero`
3. Configura:
   - **Project Name**: bazar-el-romero
   - **Framework Preset**: Other
   - **Build Command**: `echo "No build required"`
   - **Output Directory**: `backend_elromero/tienda/templates/tienda`
4. Haz clic en **Deploy** y espera a que termine

## Paso 6: Configurar el Frontend
1. En Vercel, ve a tu proyecto > **Settings** > **Environment Variables**
2. Agrega una variable `API_URL` con la URL de tu backend (ej: `https://bazar-el-romero-api.onrender.com/api`)
3. Haz clic en **Save** y re-deploya el proyecto

## Paso 7: Acceder a la Tienda
- **Frontend**: Tu dominio de Vercel (ej: `bazar-el-romero.vercel.app`)
- **Admin**: URL del backend + `/admin` (ej: `https://bazar-el-romero-api.onrender.com/admin`)

## Paso 8: Usar la Tienda
### Agregar Productos
1. Abre el admin con las credenciales que creaste
2. Ve a **Productos** > **Agregar producto**
3. Completa los campos y guarda
4. Los productos se mostrarán automáticamente en la tienda

### Desactivar Productos
1. En el admin, ve a **Productos**
2. En la lista, desmarca el checkbox **Activo**
3. Guarda los cambios
4. El producto no se mostrará más en la tienda

### Verificar Disponibilidad
- Los productos con stock > 0 se marcan como "Disponible"
- Los productos con stock = 0 se marcan como "Agotado"

## Mantenimiento
- **Actualizaciones**: Cuando hagas cambios en el código, sube los cambios a GitHub y Render/Vercel lo actualizarán automáticamente
- **Backups**: Render hace backups automáticos de la base de datos
- **Support**: Si tienes problemas, revisa la documentación de Render y Vercel

## Notas Importantes
- El servicio gratuito de Render tiene límites de uso (100GB de ancho de banda / mes, 512MB de RAM)
- El servicio gratuito de Vercel es ilimitado para proyectos pequeños
- Asegúrate de no compartir tu clave secreta de Django

## Troubleshooting
### Productos no se muestran
- Verifica que el backend esté corriendo
- Verifica la variable `API_URL` en Vercel
- Verifica que los productos estén activos y con stock > 0

### Error de conexión
- Verifica que el backend esté deployado
- Verifica la URL del backend en Vercel
- Verifica que la base de datos esté conectada
