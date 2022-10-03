from rest_framework import serializers
from inventarioApp.models.client import Client
from inventarioApp.models.purchase import Purchase
from inventarioApp.serializers.purchaseSerializer import PurchaseSerializer

class ClientSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer()
    class Meta:
        model = Client
        fields = ['id', 'username', 'password', 'name', 'email', 'age', 'phone', 'purchase']

    def getUserName():
        client =  Client.objects.all()
        return {
            'username': client.username
        }
    def getNameClient():
        client = Client.objects.all()
        return {
            'name': client.name,
            'last_name': client.last_name,
        }    

    def create(self, validated_data):
        purchaseData = validated_data.pop('purchase')
        clientInstance = Client.objects.create(**validated_data)
        Purchase.objects.create(client=clientInstance, **purchaseData)
        return clientInstance

    def to_representation(self, obj):
        client = Client.objects.get(id=obj.id)
        purchase = Purchase.objects.get(cliente=obj.id)       
        return {
                    'id': client.id, 
                    'username': client.username,
                    'name': client.name,
                    'email': client.email,
                    'age': client.age,
                    'phone': client.phone,
                    'purchase': {
                        'id': purchase.id,
                        'totalValue': purchase.totalValue,
                        'purchaseDate': purchase.purchaseDate,
                        'product': purchase.product
                    }
                }
    def totalValuePurchaseClient(self, obj):
        client = Client.objects.get(id=obj.id)
        purchase = Purchase.objects.get(cliente=obj.id)       
        return {
                    'name': client.name,
                    'purchase': {                        
                        'totalValue': purchase.totalValue,                                                
                    }
                }