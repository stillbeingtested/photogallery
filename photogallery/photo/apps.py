from django.apps import AppConfig


class PhotoConfig(AppConfig):
    name = 'photo'

    def ready(self):
        print('intializing app')
        import photo.signals
