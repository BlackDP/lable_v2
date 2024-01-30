from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofile'
    verbose_name = 'Профили пользователей'
    
    
    def ready(self):
        import userprofile.signals  # noqa: F401

