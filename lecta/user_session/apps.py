from django.apps import AppConfig


class UserSessionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_session"

    def ready(self):
        from user_session.api.v1.services import signals
