from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BodySignal,  FellChair
from notification.utils import send_notification


@receiver(post_save)
def signal_receiver(sender, weak=False, **kwargs):
    if issubclass(sender, BodySignal):
        body_signal = kwargs.get('instance')
        if not body_signal.is_critical:
            return
        send_notification(body_signal)

    elif issubclass(sender, FellChair):
        signal = kwargs.get('instance')
        send_notification(signal, "O paciente {0} caiu da Cadeira")
