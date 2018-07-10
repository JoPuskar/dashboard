import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import Data

gorkha = requests.get('http://127.0.0.1:8000/visualizations/api/data/')

# nuwakot = requests.get('http://127.0.0.1:8000/visualizations/api/data/')
# print(r.json())


class Command(BaseCommand):
    help = 'Synchronizes the database with data coming from the api.'

    def handle(self, *args, **options):
        try:
            if gorkha.json():
                for data in gorkha.json():
                    Data.objects.filter(gaunpalika__name=data['gaunpalika_name']).update(\
                        houses_in_stage_i=data['houses_in_stage_i'], houses_in_stage_ii=data['houses_in_stage_ii'],\
                        houses_in_stage_iii=data['houses_in_stage_iii'], received_tranche_i=data['received_tranche_i'],\
                        received_tranche_ii=data['received_tranche_ii'], received_tranche_iii=data['received_tranche_iii'],\
                        total_houses=data['total_houses'], houses_completed=data['houses_completed'],\
                        number_of_women=data['number_of_women'], source_is_fieldSight=False)
                    print("here")

            # if nuwakot.json():
            #     print(nuwakot.json())
            #     for data in nuwakot.json():
            #         Data.objects.filter(gaunpalika__name=data.gaunpalika_name).update(\
            #             houses_in_stage_i=data.houses_in_stage_i, houses_in_stage_ii=data.houses_in_stage_ii,\
            #             houses_in_stage_iii=data.houses_in_stage_iii, received_tranche_i=data.received_tranche_i,\
            #             received_tranche_ii=data.received_tranche_ii, received_tranche_iii=data.received_tranche_iii,\
            #             total_houses=data.total_houses, houses_completed=data.houses_completed,\
            #             number_of_women=data.number_of_women,)
        except:
            raise CommandError('No data available.')

        self.stdout.write(self.style.SUCCESS('Successfully updated database'))