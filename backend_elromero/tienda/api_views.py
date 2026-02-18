from rest_framework import viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer

# View to get products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# View to process the cart
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        # Add logic for processing cart
        serializer.save()

# Function to validate products
def validate_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return True, product
    except Product.DoesNotExist:
        return False, None
