from rest_framework import serializers
from .models import CoreService, WeProvide

class CoreServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreService
        fields = '__all__'

class WeProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeProvide
        fields = '__all__'