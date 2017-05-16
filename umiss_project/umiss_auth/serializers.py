from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal
from .models import CustomUser, MonitorUser, PatientUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username')


class MonitorUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonitorUser
        fields = ('url', 'username', 'password')

    def create(self, validated_data):
        user = MonitorUser.objects.create_user(**validated_data)
        return user

class PatientUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientUser
        fields = ('url', 'username', 'password')

    def create(self, validated_data):
        user = PatientUser.objects.create_user(**validated_data)
        return user
