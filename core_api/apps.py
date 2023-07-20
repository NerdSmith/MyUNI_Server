from django.apps import AppConfig
from django.db.models.signals import post_migrate

from core_api.signals import populate_groups


class CoreApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_api'

    def ready(self):
        post_migrate.connect(populate_groups, sender=self)
