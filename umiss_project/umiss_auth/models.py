from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    token = models.CharField(
        max_length=512,
        null=True
    )

    def get_monitor_tokens(self):
        return [monitor.android_token for monitor in self.monitors.all()]


class PatientUser(CustomUser):
    pass


class Monitor(CustomUser):
    android_token = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )

    monitor_user = models.ForeignKey(
        'umiss_auth.CustomUser',
        related_name='monitors',
        on_delete=models.SET_NULL,
        null=True,
    )

    __original_token = None

    def __init__(self, *args, **kwargs):
        # patient = PatientUser.objects.filter(token=kwargs['token'])
        # print(args, kwargs, patient)
        super(CustomUser, self).__init__(*args, **kwargs)
        self.__original_token = self.token

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """Adding a monitor to a patient if the token can be same"""

        super(
            CustomUser,
            self).save(
            force_insert,
            force_update,
            *
            args,
            **kwargs)

        qs_patient = PatientUser.objects.filter(token=self.token)
        if len(qs_patient):
            patient = qs_patient[0]
            patient.monitors.add(self)
            patient.save()
        else:
            try:
                self.monitor_user.monitors.remove(self)
            except AttributeError:
                pass
        self.__original_token = self.token

    def get_patients_tokens(self):
        return [patient.token for patient in PatientUser.objects.all()]
