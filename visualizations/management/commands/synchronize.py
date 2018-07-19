import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import Data

gorkha_data = requests.get('http://rims.southeastasia.cloudapp.azure.com:8085/dataForNaxa')

nuwakot_data = requests.get('https://app.fieldsight.org/fieldsight/api/municipality/')


class Command(BaseCommand):
    help = 'Synchronizes the database with data coming from the api.'

    def handle(self, *args, **options):
        try:
            if gorkha_data.json():
                [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                    houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                    houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                    received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                    total_houses=data['total_houses'], women_percentage=round(float(data['women_percentage'])), source_is_fieldSight=False)
                    for data in gorkha_data.json()]

            if nuwakot_data.json():
                [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                    houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                    houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                    received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                    total_houses=data['total_houses'], houses_completed=data['houses_completed'], women_percentage=0,)
                    for data in nuwakot_data.json()]
        except:
            raise CommandError('No data available.')

        self.stdout.write(self.style.SUCCESS('Successfully updated database'))