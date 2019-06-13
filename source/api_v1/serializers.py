from webapp.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:user-detail')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'md5', 'sha1', 'sha256', 'all_user_data')
