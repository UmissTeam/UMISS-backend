from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BodySignal


@receiver(post_save)
def signal_receiver(sender, weak=False, **kwargs):
    if not issubclass(sender, BodySignal):
        return

    body_signal = kwargs.get('instance')
    monitors = body_signal.owner.monitors.all()
    for monitor in monitors:
        print('Hello {0.username}'.format(monitor))
