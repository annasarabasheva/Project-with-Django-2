from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PersonalProject.accounts'

    def ready(self):
        import PersonalProject.accounts.signals