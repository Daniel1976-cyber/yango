from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen', 'fecha_creacion', 'activo', 'categoria', 'categoria_nombre']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.imagen:
            if request:
                representation['imagen'] = request.build_absolute_uri(instance.imagen.url)
            else:
                representation['imagen'] = instance.imagen.url
        
        # Add 'img' field for frontend compatibility (matches Supabase explicit table field name)
        representation['img'] = representation.get('imagen')
        
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