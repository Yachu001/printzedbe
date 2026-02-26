from rest_framework import serializers
from .models import MarketingSolution, Portfolio, TeamMember

class MarketingSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingSolution
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'