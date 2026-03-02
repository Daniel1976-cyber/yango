# Configuración de Supabase para el Frontend

## Paso 1: Obtener credenciales de Supabase

1. Ve a [Supabase.com](https://supabase.com) e inicia sesión
2. Selecciona tu proyecto
3. Ve a **Settings** (⚙️) → **API**
4. Copia:
   - **Project URL**: algo como `https://xyzabc.supabase.co`
   - **anon public key**: una cadena larga que empieza con `eyJ...`

## Paso 2: Editar el frontend

Abre `backend_elromero/frontend/index.html` y reemplaza:
```javascript
const SUPABASE_URL = 'https://[TU_PROYECTO].supabase.co';
const SUPABASE_KEY = 'TU_API_KEY';
```

Con tus datos reales:
```javascript
const SUPABASE_URL = 'https://xyzabc.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
```

## Paso 3: Subir a Vercel

1. Guarda los cambios
2. Sube a GitHub
3. Vercel se redeplegará automáticamente

## Verificar

- Accede a https://yango-omega.vercel.app
- Los productos de Supabase deberían aparecer

## Notas

- La tabla en Supabase debe llamarse `productos`
- Las columnas necesarias: id, nombre, precio, categoria, disponible, img, active
- Los productos con `active = true` se mostrarán en la tienda
