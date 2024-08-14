from django.apps import AppConfig
from django.db.models.signals import post_migrate


def seed_data(sender, **kwargs):
    from django.core.management import call_command
    call_command('seed')


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(seed_data, sender=self)
