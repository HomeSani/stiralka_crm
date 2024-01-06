from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Устанавливает для всех пользователей restriction_on_use_count равным 2"

    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            user.restriction_on_use_count = 2
            user.save()
