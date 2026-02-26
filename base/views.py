from django.shortcuts import render
from rest_framework import viewsets
from .models import MarketingSolution, Portfolio, TeamMember
from .serializers import *

# Create your views here.
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Backend is live 🚀"})

class MarketingSolutionsViewSet(viewsets.ModelViewSet):
    queryset = MarketingSolution.objects.all()
    serializer_class = MarketingSolutionSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer