import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import Data

r = requests.get('http://127.0.0.1:8000/visualizations/api/data/')

# print(r.json())


class Command(BaseCommand):
    help = 'Synchronizes the database by populating database with data coming from the api.'

    def handle(self, *args, **options):
        try:
            if r.json():
                print(r.json())
                for data in r.json():
                    Data.objects.get_or_create(data)
        except:
            raise CommandError('No data available.')

        self.stdout.write(self.style.SUCCESS('Successfully updated database'))