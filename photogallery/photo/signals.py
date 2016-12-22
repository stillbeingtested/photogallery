from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Photo, Like


@receiver(pre_save, sender=Photo)
def process_photo_tag(sender, instance, **kwargs):
    photo = instance
    all_tags = photo.tags.all()
    has_blocking = False
    for t in all_tags:
        if t.is_blocking:
            has_blocking = True

    photo.blocked_by_tag = has_blocking


@receiver(post_save, sender=Like)
def update_like_count(sender, instance, **kwargs):
    photo = instance.photo
    photo.like_count += 1
    photo.save()