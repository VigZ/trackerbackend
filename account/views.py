from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .models import User, Team
from .serializers import UserSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AnonCreateAndUpdateOwnerOnly, ListAdminOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token =  User.objects.get(email=serializer.data.get('email')).token
        data_dict = {'auth_token':token.__str__()}
        data_dict.update(serializer.data)
        return Response(data_dict, status=status.HTTP_201_CREATED, headers=headers)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
