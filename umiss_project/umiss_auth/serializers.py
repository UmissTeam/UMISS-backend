from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal
from .models import CustomUser, MonitorUser, PatientUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username')


class MonitorUserSerializer(UserSerializer):
    class Meta:
        model = MonitorUser

class PatientUserSerializer(UserSerializer):
    class Meta:
        model = PatientUser
