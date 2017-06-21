from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal, GalvanicResistance, SkinTemperature, FellChair
from django.contrib.auth.models import User

class FellChairSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FellChair
        fields = ('owner', 'created')

class HeartBeatsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = HeartBeats
        fields = ('owner', 'created', 'beats', 'is_critical')


class GalvanicResistanceSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GalvanicResistance
        fields = ('owner', 'created', 'resistance', 'is_critical')


class SkinTemperatureSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SkinTemperature
        fields = ('owner', 'created', 'temperature', 'is_critical')
