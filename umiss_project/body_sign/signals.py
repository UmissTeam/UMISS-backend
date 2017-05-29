from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BodySignal
from notification.utils import send_notification


@receiver(post_save)
def signal_receiver(sender, weak=False, **kwargs):
    if not issubclass(sender, BodySignal):
        return

    body_signal = kwargs.get('instance')
    if not body_signal.is_critical:
        return
    send_notification(body_signal)
