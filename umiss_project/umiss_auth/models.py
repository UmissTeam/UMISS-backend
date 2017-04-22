from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    type_choices = (
        ('patient', 'User Type Pacient'),
        ('monitor', 'User Type Monitor'),
    )

    user_type = models.CharField(
        max_length=2,
        choices=type_choices,
        default='monitor'
    )

    token = models.CharField(max_length=512, editable=False)

    monitor_users = models.ForeignKey(
        'umiss_auth.CustomUser',
        related_name='monitors',
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to=models.Q(user_type='monitor')
    )

    def save(self, *args, **kwargs):
        self.token = hashlib.sha512(
            self.token.encode('utf-8')
        ).hexdigest()

        super(CustomUser, self).save(*args, **kwargs)

    def get_monitor_tokens(self):
        tokens = []
        for monitor in self.monitors.all():
            tokens.append(monitor.token)

        return tokens
