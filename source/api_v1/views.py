from webapp.models import User
from rest_framework import viewsets
from api_v1.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
