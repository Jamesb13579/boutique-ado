from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_0n_save(sender, instance, created, **kwargs):
    """
    Update order total on lineorder update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_0n_save(sender, instance, **kwargs):
    """
    Update order total on lineorder delete
    """
    instance.order.update_total()