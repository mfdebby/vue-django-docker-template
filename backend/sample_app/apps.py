from django.apps import AppConfig


class SampleAppConfig(AppConfig):  # type: ignore[misc]
    default_auto_field = "django.db.models.BigAutoField"
    name = "sample_app"
