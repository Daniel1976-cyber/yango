from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    # Ya no es un ForeignKey, así que lo manejamos como un campo de lectura/escritura normal
    categoria_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen', 'fecha_creacion', 'activo', 'categoria', 'categoria_nombre']
    
    def get_categoria_nombre(self, obj):
        # En el esquema B simple, la categoría ya es el nombre
        return obj.categoria

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # En el esquema B simple, 'imagen' ya es una URL (string)
        img_url = representation.get('imagen')
        
        # Aseguramos que 'img' y 'imagen' tengan el mismo valor para el frontend
        representation['img'] = img_url
        representation['imagen'] = img_url
        
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