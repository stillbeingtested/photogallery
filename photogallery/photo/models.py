from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    is_blocking = models.BooleanField(default=False)


class Photo(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, related_name='photos')
    href = models.URLField()
    created_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='photos')
    blocked_by_tag = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)


class Like(models.Model):
    photo = models.ForeignKey(Photo, null=False, blank=False, related_name='likes')
    user = models.ForeignKey(User, null=False, blank=False, related_name='likes')

