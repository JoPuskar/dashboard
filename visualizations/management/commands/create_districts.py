import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import District, Gaunpalika


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):
        if District.objects.filter(name='Gorkha') is None:
            District.objects.create(name='Gorkha')
        else:
            self.stdout.write(self.style.WARNING('Gorkha District Already Created!'))

        if District.objects.filter(name='Nuwakot') is None:
            District.objects.create(name='Nuwakot')
        else:
            self.stdout.write(self.style.WARNING('Nuwakot District Already Created!'))

        self.stdout.write(self.style.SUCCESS('Successfully Created Gorkha And Nuwakot Districts!'))