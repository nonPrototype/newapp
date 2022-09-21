from rest_framework import viewsets, permissions
from authApp.models.person import Persona
from authApp.serializers.personSerializer import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]
