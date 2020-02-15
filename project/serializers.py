from django.shortcuts import get_object_or_404
from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Project, Ticket, Tag, TicketGrouping, Comment
from account.models import User


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'name', 'poster', 'assigned_to', 'description',
        'attachment', 'tags', 'due_date', 'completed_date', 'severity',
        'priority', 'steps_to_reproduce', 'ticket_grouping']


class TicketGroupingSerializer(serializers.HyperlinkedModelSerializer):
    ticket_set = TicketSerializer(read_only=True, many=True)
    class Meta:
        model = TicketGrouping
        fields = ['url', 'name', 'project', 'resolution_order', 'ticket_set',]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    admins = UserSerializer(many=True, required=False)
    members = UserSerializer(many=True, required=False)
    ticketgrouping_set = TicketGroupingSerializer(read_only=True, many=True)

    def create(self, validated_data):
        name = validated_data.get('project_name')
        project_creator = validated_data.get('owner')
        new_project = Project.objects.create(project_name=name, owner=project_creator)
        new_project.admins.add(project_creator)
        new_project.members.add(project_creator)
        return new_project

    class Meta:
        model = Project
        fields = ['url', 'project_name', 'owner', 'admins', 'members', 'ticketgrouping_set',]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'name']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'poster', 'ticket', 'created_at', 'comment_text',]

    def create(self, validated_data):
        ticket = validated_data.get('ticket')
        poster = validated_data.get('poster')
        comment_text = validated_data.get('comment_text')
        new_comment = Comment.objects.create(ticket=ticket, poster=poster, comment_text=comment_text)
        return new_comment
