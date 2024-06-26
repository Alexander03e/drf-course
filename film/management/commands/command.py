from django.core.management.base import BaseCommand
from authentication.models import User
class Command(BaseCommand):
    help = "Display all users"

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            self.stdout.write(f"Username: {user.username}, Email: {user.email}")