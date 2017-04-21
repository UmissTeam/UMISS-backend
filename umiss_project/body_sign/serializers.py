from rest_framework import serializers
from body_sign.models import HeartBeats, BodySignal
from django.contrib.auth.models import User


class HeartBeatsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = HeartBeats
        fields = ('owner', 'created', 'beats')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    bodysignals = serializers.HyperlinkedRelatedField(queryset=BodySignal.objects.all(), view_name='bodysign-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'bodysignals')
