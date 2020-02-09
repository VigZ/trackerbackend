from rest_framework import serializers
from .models import Project, Ticket, Tag


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'project_name', 'owner', 'admins', 'members']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'name', 'poster', 'assigned_to', 'description', 'attachment', 'tags']
