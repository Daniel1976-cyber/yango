from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.imagen:
            representation['imagen'] = f"http://127.0.0.1:8000{instance.imagen.url}"
        
        # Agregar campo disponible basado en stock y estado activo
        representation['disponible'] = instance.stock > 0 and instance.activo
        
        # Agregar campo active que refleja el estado del producto
        representation['active'] = instance.activo
        
        return representation

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pedido
        fields = '__all__'