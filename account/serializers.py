from rest_framework import serializers
from .models import User, Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    teams = TeamSerializer(many=True, required=False)
    display_name = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['url', 'display_name', 'email', 'teams']
