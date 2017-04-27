from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    token = models.CharField(
        max_length=512,
        editable=False,
        null=False
    )

    def save(self, *args, **kwargs):
        self.token = hashlib.sha512(
            self.token.encode('utf-8')
        ).hexdigest()

        super(CustomUser, self).save(*args, **kwargs)


class PatientUser(CustomUser):
    monitor_users = models.ForeignKey(
        'umiss_auth.CustomUser',
        related_name='monitors',
        on_delete=models.SET_NULL,
        null=True,
    )

    def get_monitor_tokens(self):
        tokens = [monitor.token for monitor in self.monitors.all()]
        return tokens


class MonitorUser(CustomUser):
    android_token = models.CharField(
        max_length=512,
        editable=True,
        null=False,
        blank=False
    )
