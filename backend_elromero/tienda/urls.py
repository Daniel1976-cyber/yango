from django.urls import path

from .views import ProductoList, CarritoList, ValidarProducto

urlpatterns = [
    path('api/productos/', ProductoList.as_view(), name='producto-list'),
    path('api/carrito/', CarritoList.as_view(), name='carrito-list'),
    path('api/validar-producto/', ValidarProducto.as_view(), name='validar-producto'),
]