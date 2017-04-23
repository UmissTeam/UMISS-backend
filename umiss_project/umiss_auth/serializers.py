from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal
from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('url', 'username')
