import time
from django.core.management.base import BaseCommand
from display_flow.models import Flow

class Command(BaseCommand):
    help = 'Ensures there is an intial value in the database'

    def handle(self, *args, **options):
        if not Flow.objects.all().exists():
            first = Flow(timestamp=int(time.time()))
            first.save()
            self.stdout.write(self.style.SUCCESS('Initialized Database'))
        else:
            self.stdout.write(self.style.SUCCESS('Database Exists'))

