from authApp.models.person import Persona
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id','nombre','apellido','edad']
    