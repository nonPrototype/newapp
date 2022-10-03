from rest_framework import viewsets, permissions
from inventarioApp.models.product import Product
from inventarioApp.serializers.productSerializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
