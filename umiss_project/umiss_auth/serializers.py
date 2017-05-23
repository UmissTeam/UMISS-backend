from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal
from .models import CustomUser, Monitor, PatientUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username')


class MonitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitor
        fields = ('url', 'username', 'password', 'android_token', 'token')

    def create(self, validated_data):
        user = Monitor.objects.create_user(**validated_data)
        return user


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class PatientUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientUser
        fields = ('url', 'username', 'password', 'token')

    def create(self, validated_data):
        user = PatientUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
