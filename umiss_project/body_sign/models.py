from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class BodySignal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('umiss_auth.CustomUser', related_name='bodysignals')

    class Meta:
        ordering = ('created',)
        # abstract = True
        
    def __str__(self):
        return "{0.__class__.__name__} created by: {0.owner}".format(self)


class HeartBeats(BodySignal):
    beats = models.IntegerField(
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)
        ]
    )

    
class GalvanicResistance(BodySignal):
    resistance = models.IntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(100)
        ]
    )

    
class SkinTemperature(BodySignal):
    temperature = models.IntegerField(
        validators=[
            MaxValueValidator(39),
            MinValueValidator(32)
        ]
    )

    
