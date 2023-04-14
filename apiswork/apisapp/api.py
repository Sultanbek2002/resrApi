from .models import Workapi
from rest_framework import viewsets,permissions
from .serializare import ApiSerializers

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Workapi.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApiSerializers