from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = "Interns"

    # def ready(self):
    #     from intern_tracker.permissions import assign_permissions
    #     assign_permissions()
