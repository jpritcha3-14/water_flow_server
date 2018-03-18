import sys
import sqlite3
import time
from django.core.management.base import BaseCommand
from display_flow.models import Flow

class Command(BaseCommand):

    help = 'writes flow data and timestamps to the db'

    def add_arguments(self, parser):
        parser.add_argument('flowrate', nargs='+', type=int)

    def handle(self, *args, **options):

        for flowrate in options['flowrate']:
            entry = Flow(val=int(flowrate), 
                         timestamp=int(time.time()))
            entry.save()

print('exiting db_writer')
