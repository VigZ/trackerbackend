from rest_framework import serializers
from .models import Project, Ticket, Tag, TicketGrouping, Comment


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        name = validated_data.get('name')
        project_creator = validated_data.user
        new_project = Project.objects.create(project_name=name, owner=project_creator)
        new_project.admins.add(project_creator)
        new_project.members.add(project_creator)
        return new_project
        
    class Meta:
        model = Project
        fields = ['url', 'project_name', 'owner', 'admins', 'members']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']


class TicketGroupingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketGrouping
        fields = ['url', 'name', 'project', 'resolution_order',]


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'name', 'poster', 'assigned_to', 'description',
                 'attachment', 'tags', 'due_date', 'completed_date', 'severity',
                 'priority', 'steps_to_reproduce', 'ticket_grouping']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'poster', 'ticket', 'created_date', 'comment_text',]
