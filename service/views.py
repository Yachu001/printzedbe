from django.shortcuts import render
from rest_framework import viewsets
from .models import CoreService, WeProvide
from .serializers import *

# Create your views here.
class CoreServiceViewSet(viewsets.ModelViewSet):
    queryset = CoreService.objects.all()
    serializer_class = CoreServiceSerializer

class WeProvideViewSet(viewsets.ModelViewSet):
    queryset = WeProvide.objects.all().order_by('index')
    serializer_class = WeProvideSerializer