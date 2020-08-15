from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
"""
    import two signals from django.db.models.signals
    post_save and post_delete.
    Post, in this case, means after.
    So this implies these signals are sent by django to the entire application
    after a model instance is saved and after it's deleted respectively.
    To receive these signals we can import receiver from django.dispatch.
    Of course since we'll be listening for signals from the OrderLineItem model
    we'll also need that.
    """


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
