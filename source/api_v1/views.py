import random
from django.db import OperationalError
from webapp.models import User
from rest_framework import viewsets
from api_v1.serializers import UserSerializer, UserShortSerializer, UserNumberSerializer


def get_random_user():
    count = User.objects.all().count()
    rand_ids = random.sample(list(range(1, count + 1)), 1)
    return rand_ids


class UserViewSet(viewsets.ModelViewSet):
    try:
        queryset = User.objects.all()
        try:
            queryset = User.objects.filter(id__in=get_random_user())
        except OperationalError:
            pass
    except ValueError:
        pass
    serializer_class = UserSerializer


class UserShortViewSet(viewsets.ModelViewSet):
    try:
        queryset = User.objects.all()
        try:
            queryset = User.objects.filter(id__in=get_random_user())
        except OperationalError:
            pass
    except ValueError:
        pass
    serializer_class = UserShortSerializer


class UserNumberViewSet(viewsets.ModelViewSet):
    try:
        queryset = User.objects.all()
        try:
            queryset = User.objects.filter(id__in=get_random_user())
        except OperationalError:
            pass
    except ValueError:
        pass
    serializer_class = UserNumberSerializer
