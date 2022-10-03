from rest_framework import viewsets, permissions
from inventarioApp.models.purchase import Purchase
from inventarioApp.serializers.purchaseSerializer import PurchaseSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.AllowAny]
