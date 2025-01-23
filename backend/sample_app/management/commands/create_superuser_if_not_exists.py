from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from loguru import logger


class Command(BaseCommand):  # type: ignore[misc]
    help = "Create a superuser if one does not exist"

    def handle(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        username = config("DJANGO_SUPERUSER_USERNAME")
        email = config("DJANGO_SUPERUSER_EMAIL")
        password = config("DJANGO_SUPERUSER_PASSWORD")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username, email=email, password=password
            )
            logger.info(f'Superuser "{username}" created.')
        else:
            logger.info(f'Superuser "{username}" already exists.')
