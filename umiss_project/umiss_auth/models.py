from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (
        ('patient', 'User Type Pacient'),
        ('monitor', 'User Type Monitor'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='monitor')
    token = models.CharField(max_length=512, editable=False)

    def save(self, *args, **kwargs):
        self.token = hashlib.sha512(self.token.encode('utf-8')).hexdigest()
        super(CustomUser, self).save(*args, **kwargs)
