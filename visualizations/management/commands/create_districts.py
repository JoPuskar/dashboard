import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import District, Gaunpalika


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):
        try:
            districts = ['Gorkha', 'Nuwakot']
            for district in districts:
                District.objects.create(name=district)
        except:
            CommandError("Command Error!")
        self.stdout.write(self.style.SUCCESS('Successfully Created Districts!'))