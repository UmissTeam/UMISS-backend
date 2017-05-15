from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer, MonitorUserSerializer, PatientUserSerializer
from .models import MonitorUser, PatientUser
from rest_framework import viewsets
from rest_framework import permissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.AllowAny, permissions.BasePermission)

class MonitorViewSet(viewsets.ModelViewSet):
    queryset = MonitorUser.objects.all()
    serializer_class = MonitorUserSerializer


class PatienteViewSet(viewsets.ModelViewSet):
    queryset = PatientUser.objects.all()
    serializer_class = PatientUserSerializer
