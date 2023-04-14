from rest_framework import serializers
from .models import Workapi


class ApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workapi
        fields = '__all__'
