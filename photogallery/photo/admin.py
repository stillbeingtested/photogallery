from django.contrib import admin

from .models import User, Tag, Photo, Like

class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

    list_display = ('name', 'is_blocking')


class PhotoAdmin(admin.ModelAdmin):
    class Meta:
        model = Photo

    list_display = ('created_date', 'href', 'blocked_by_tag')

admin.site.register(User)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Like)