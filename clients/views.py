from django.shortcuts import render
from rest_framework import viewsets
from .models import FeaturedWorks, Review
from .serializers import *

# Create your views here.
class FeaturedWorksViewSet(viewsets.ModelViewSet):
    queryset = FeaturedWorks.objects.all()
    serializer_class = FeaturedWorksSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer