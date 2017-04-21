from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BodySignal

@receiver(post_save)
def signal_receiver(sender, weak=False, **kwargs):
    if not issubclass(sender, BodySignal):
        return

    print("Created object!", kwargs)
