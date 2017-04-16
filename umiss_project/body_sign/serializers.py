from rest_framework import serializers
from body_sign.models import BodySignal
from django.contrib.auth.models import User


class BodySignalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BodySignal
        fields = ('owner', 'created', 'type_signal')
                  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    bodysignals = serializers.HyperlinkedRelatedField(queryset=BodySignal.objects.all(), view_name='bodysign-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'bodysignals')
