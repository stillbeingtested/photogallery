from urllib.parse import urlencode

from django.template.defaulttags import register
from django.views.generic import ListView

from .models import Photo, Tag


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


class PhotoView(ListView):
    model = Photo
    template_name = "photo_list.html"
    paginate_by = 20

    def get_queryset(self):
        tags_string = self.request.GET.get('tags', '')
        tags_filtering = tags_string.split(',') if tags_string else []
        date_order = self.request.GET.get('date', 'desc')
        like_order = self.request.GET.get('likes', 'desc')
        orderings = []
        if date_order is not None:
            date_db_ordering = 'created_date' if date_order == 'asc' else '-created_date'
            orderings.append(date_db_ordering)

        if like_order is not None:
            like_db_ordering = 'like_count' if like_order == 'desc' else '-like_count'
            orderings.append(like_db_ordering)

        queryset = Photo.objects.filter(blocked_by_tag=False)
        if tags_filtering:
            tags = Tag.objects.filter(name__in=tags_filtering)
            queryset = queryset.filter(tags__in=tags)

        queryset.order_by(*orderings)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['tags'] = self.request.GET.get('tags', [])
        context['date'] = self.request.GET.get('date', 'desc')
        context['likes'] = self.request.GET.get('likes', 'desc')
        return context
