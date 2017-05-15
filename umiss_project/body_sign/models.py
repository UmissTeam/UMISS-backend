from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class BodySignal(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        'umiss_auth.CustomUser',
        related_name='bodysignals',
        on_delete=models.CASCADE
    )

    is_critical = models.BooleanField(
        blank=False,
        null=False,
        editable=False,
        default=False,
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{0.__class__.__name__} created by: {0.owner}".format(self)


class HeartBeats(BodySignal):
    beats = models.IntegerField(
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)
        ]
    )

    def message(self):
        """O paciente {0.owner} está com sinais alterados \
        de Batimentos cardíacos com {0.beats}""".format(self)


class GalvanicResistance(BodySignal):
    resistance = models.IntegerField(
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(100)
        ]
    )

    def message(self):
        """O paciente {0.owner} está com sinais alterados \
        de Estresse com {0.resistance}""".format(self)


class SkinTemperature(BodySignal):
    temperature = models.IntegerField(
        validators=[
            MaxValueValidator(39),
            MinValueValidator(32)
        ]
    )

    def message(self):
        """O paciente {0.owner} está com sinais alterados \
        de Temperatra corporal com {0.temperature}""".format(self)
