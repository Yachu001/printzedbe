from rest_framework import serializers
from .models import FeaturedWorks, Review

class FeaturedWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedWorks
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'