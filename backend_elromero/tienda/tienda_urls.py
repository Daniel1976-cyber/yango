from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import tienda_views as views
from .supabase_api import productos_api, agregar_producto_api

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'pedidos', views.PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('supabase/productos/', productos_api, name='supabase_productos'),
    path('supabase/productos/agregar/', agregar_producto_api, name='supabase_agregar_producto'),
]