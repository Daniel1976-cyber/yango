# Pasos para Deployar el Backend en Render

## Paso 1: Subir código a GitHub
1. Crea un repositorio en GitHub (si no lo tienes)
2. Sube la carpeta `backend_elromero` a GitHub
3. Asegúrate de incluir todos los archivos

## Paso 2: Crear Web Service en Render
1. Ve a [Render.com](https://render.com/) e inicia sesión
2. Click en **New** → **Web Service**
3. Conecta tu repositorio de GitHub
4. Configura:
   - **Name**: `yango-backend` (o el nombre que prefieras)
   - **Region**: Frankfurt (o closest a tu ubicación)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backend_elromero.wsgi:application`

## Paso 3: Configurar Variables de Entorno
En la sección **Environment** de Render, agrega:

| Variable | Valor |
|----------|-------|
| `SECRET_KEY` | Copia la clave de settings.py o genera una nueva |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `yango-backend.onrender.com` |
| `SUPABASE_URL` | Tu URL de Supabase: `postgresql://postgres:[PASSWORD]@db.[PROYECTO].supabase.co:5432/postgres` |

**Para obtener tu SUPABASE_URL:**
1. Ve a Supabase → Settings → Database
2. Copia la "Connection String"
3. Reemplaza `[PASSWORD]` con tu contraseña de Supabase

## Paso 4: Ejecutar Migraciones
1. En Render, ve a tu Web Service → **Shell**
2. Ejecuta:
   ```
   python manage.py migrate
   ```

## Paso 5: Actualizar el Frontend
1. Ve a tu proyecto en Vercel
2. En Settings → Environment Variables
3. Agrega: `API_URL` = `https://yango-backend.onrender.com/api`
4. Redeploy el proyecto

## Verificar
- Backend: `https://yango-backend.onrender.com/api/supabase/productos/`
- Frontend: `https://yango-omega.vercel.app/`
