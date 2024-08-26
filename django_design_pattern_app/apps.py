from django.apps import AppConfig


class DjangoDesignPatternAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_design_pattern_app'


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import django_design_pattern_app.models


class HelloappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "helloapp"

    def ready(self):
        from django_design_pattern_app.signals import receivers
