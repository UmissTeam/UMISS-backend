from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    token = models.CharField(
        max_length=512,
        null=True
    )



class PatientUser(CustomUser):
    monitor_users = models.ForeignKey(
        'umiss_auth.CustomUser',
        related_name='monitors',
        on_delete=models.SET_NULL,
        null=True,
    )


    def get_monitor_tokens(self):
        return [monitor.token for monitor in self.monitors.all()]


class MonitorUser(CustomUser):
    android_token = models.CharField(
        max_length=512,
        null=True,
        blank=True
    ) 

    __original_token = None

    def __init__(self, *args, **kwargs):
        super(CustomUser, self).__init__(*args, **kwargs)
        self.__original_token = self.token

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """Adding a monitor to a patient if the token can be same"""
        if self.token != self.__original_token:
            patient = PatientUser.objects.filter(token=self.token)
            if len(patient):
                self.monitors.add(patient[0])
            else:
                self.monitors.clear()

        super(CustomUser, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_token = self.token

    def get_patients_tokens(self):
        return [patient.token for patient in PatientUser.objects.all()]
