from .serializers import User, UserSerializer, Group, GroupSerializer
from rest_framework import viewsets, permissions


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """Endpoint da API que permite que os usuários sejam visualizados ou editados."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """Endpoint da API que permite que grupos sejam visualizados ou editados."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
