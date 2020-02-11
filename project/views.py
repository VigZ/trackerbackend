from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Project, Ticket, Tag, TicketGrouping, Comment
from .serializers import ProjectSerializer, TagSerializer, TicketSerializer, TicketGroupingSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request):
        name = request.POST.get('name')
        project_creator = request.user
        new_project = Project.objects.create(project_name=name, owner=project_creator)
        new_project.admins.add(project_creator)
        new_project.members.add(project_creator)
        new_project.save()

        return Response(status=status.HTTP_201_CREATED)



class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketGroupingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TicketGrouping.objects.all()
    serializer_class = TicketGroupingSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
