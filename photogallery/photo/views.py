from django.views.generic import ListView

from .models import Photo


class PhotoView(ListView):
    model = Photo
    template_name = "photo_list.html"
    paginate_by = 20

    def get_queryset(self):
        tag_filtering = self.request.GET.get('tags', [])
        date_order = self.request.GET.get('date', 'desc')
        like_order = self.request.GET.get('likes')
        queryset = Photo.objects
        if date_order is not None:
            date_db_ordering = 'created_date' if date_order == 'asc' else '-created_date'
            queryset = queryset.order_by(date_db_ordering)

        # if like_order is not None:
        #     like_db_ordering = 'likes'
            # pass
            # queryset.order_by(order)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['tags'] = self.request.GET.get('tags', [])
        context['date'] = self.request.GET.get('date', 'desc')
        context['likes'] = self.request.GET.get('likes')
        return context
