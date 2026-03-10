from django.apps import AppConfig


class TestFormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_form'
    verbose_name = 'Test Form App'
