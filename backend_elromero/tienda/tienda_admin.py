from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('activo',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'estado', 'total')
    list_filter = ('estado', 'fecha_pedido')

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido)