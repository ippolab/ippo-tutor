from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'ippo_tutor.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import ippo_tutor.apps.authentication.signals


default_app_config = 'ippo_tutor.apps.authentication.AuthenticationConfig'
