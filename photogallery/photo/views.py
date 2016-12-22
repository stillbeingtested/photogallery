from django.views.generic import ListView

from .models import Photo


class PhotoView(ListView):
    model = Photo
    template_name = "photo_list.html"
    paginate_by = 20
