from django.db import models

class BodySignal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='bodysignals')
    type_signal = models.CharField(
            max_length=100,
            blank=False,
            default='Batimentos')


    class Meta:
        ordering = ('created',)
