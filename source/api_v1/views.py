import random
# import re
from webapp.models import User
from rest_framework import viewsets
from api_v1.serializers import UserSerializer, UserShortSerializer, UserNumberSerializer


def get_random():
    count = User.objects.all().count()
    rand_ids = random.sample(list(range(1, count + 1)), 1)
    return rand_ids


# def get_number_from_hash():
#     queryset = User.objects.filter(id__in=get_random())
#     d = queryset.values('md5')[0].values()
#     number = re.findall(r'\d+', str(d))
#     print(number)
#     return number


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random())
    serializer_class = UserSerializer


class UserShortViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random())
    serializer_class = UserShortSerializer


class UserNumberViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(id__in=get_random())
    serializer_class = UserNumberSerializer
