import os
import psycopg2
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Función para conectar a Supabase
def get_supabase_connection():
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        return None
    
    # Parsear la URL de Supabase
    # Formato: postgresql://postgres:password@host:port/database
    try:
        conn = psycopg2.connect(database_url)
        return conn
    except Exception as e:
        print(f"Error conectando a Supabase: {e}")
        return None

@csrf_exempt
@require_http_methods(["GET"])
def productos_api(request):
    """
    API para obtener productos de Supabase
    """
    conn = get_supabase_connection()
    
    if not conn:
        # Si no hay conexión a Supabase, devolver error
        return JsonResponse({
            'error': 'No hay conexión a la base de datos',
            'productos': []
        }, status=500)
    
    try:
        cursor = conn.cursor()
        
        # Obtener productos activos
        cursor.execute("""
            SELECT id, nombre, precio, categoria, disponible, img, active 
            FROM productos 
            WHERE active = true
            ORDER BY id DESC
        """)
        
        rows = cursor.fetchall()
        
        productos = []
        for row in rows:
            producto = {
                'id': row[0],
                'nombre': row[1],
                'precio': float(row[2]) if row[2] else 0,
                'categoria': row[3],
                'disponible': row[4],
                'img': row[5],
                'active': row[6]
            }
            productos.append(producto)
        
        cursor.close()
        conn.close()
        
        return JsonResponse({'productos': productos})
    
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'productos': []
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def agregar_producto_api(request):
    """
    API para agregar un producto a Supabase
    """
    try:
        data = json.loads(request.body)
    except:
        data = request.POST.dict()
    
    conn = get_supabase_connection()
    
    if not conn:
        return JsonResponse({'error': 'No hay conexión a la base de datos'}, status=500)
    
    try:
        cursor = conn.cursor()
        
        # Insertar producto
        cursor.execute("""
            INSERT INTO productos (id, nombre, precio, categoria, disponible, img, active)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data.get('id'),
            data.get('nombre'),
            data.get('precio'),
            data.get('categoria'),
            data.get('disponible', True),
            data.get('img'),
            data.get('active', True)
        ))
        
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        
        return JsonResponse({'success': True, 'id': new_id})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
