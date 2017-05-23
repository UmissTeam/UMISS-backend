from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer, MonitorSerializer, PatientUserSerializer
from .models import Monitor, PatientUser
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsAnonCreate


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    write_only_fields = ('password',)

    permission_classes = (IsAnonCreate,)

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    write_only_fields = ('password')

    permission_classes = (IsAnonCreate,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        return self.request.user

class PatienteViewSet(viewsets.ModelViewSet):
    queryset = PatientUser.objects.all()
    serializer_class = PatientUserSerializer
    write_only_fields = ('password',)

    permission_classes = (IsAnonCreate,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


