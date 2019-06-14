import random
import re
from webapp.models import User
from rest_framework import viewsets
from api_v1.serializers import UserSerializer, UserShortSerializer, UserNumberSerializer


def get_random_user():
    count = User.objects.all().count()
    rand_ids = random.sample(list(range(1, count + 1)), 1)
    return rand_ids


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random_user())
    serializer_class = UserSerializer


class UserShortViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random_user())
    serializer_class = UserShortSerializer


def get_number_from_hash():
    queryset = User.objects.filter(id__in=get_random_user())
    d = queryset.values('md5')[0].values()
    number = re.findall(r'\d+', str(d))
    print(number)
    return number


get_number_from_hash()


class UserNumberViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random_user())
    serializer_class = UserNumberSerializer
