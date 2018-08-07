import requests

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from visualizations.models import Data, Gaunpalika, District

gorkha_data = requests.get('http://rims.southeastasia.cloudapp.azure.com:8085/dataForNaxa')

nuwakot_data = requests.get('https://app.fieldsight.org/fieldsight/api/municipality/')


class Command(BaseCommand):
    help = 'Synchronizes the database with data coming from the api.'

    def handle(self, *args, **options):
        try:
            if gorkha_data.json():
                print(gorkha_data.json())
                    # [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                #     houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                #     houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                #     received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                #     total_houses=data['total_houses'], women_percentage=round(float(data['women_percentage'])), source_is_fieldSight=False)
                #     for data in gorkha_data.json()]
                data_gorkha = gorkha_data.json()
                with transaction.atomic():
                    for d in data_gorkha:
                        gaunpalika = d['Municipality']
                        if gaunpalika == "None":
                            continue
                        print(gaunpalika)
                        obj = Data.objects.get(gaunpalika__name=gaunpalika)
                        obj.received_tranche_i = d["received_trache_i"]
                        obj.received_tranche_ii = d["received_trache_ii"]
                        obj.received_tranche_iii = d["received_trache_iii"]

                        obj.houses_in_stage_i = d["house_in_stage_i"]
                        obj.houses_in_stage_ii = d["house_in_stage_ii"]
                        obj.houses_in_stage_iii = d["house_in_stage_iii"]
                        obj.houses_in_stage_iii = d["house_in_stage_iii"]

                        obj.houses_completed = d["houses_completed"]
                        obj.total_houses = d["total_houses"]
                        obj.women_percentage = round(float(d['women_percentage']))
                        print(obj.__dict__)
                        obj.save()

            if nuwakot_data.json():
                # [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                #     houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                #     houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                #     received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                #     total_houses=data['total_houses'], houses_completed=data['houses_completed'], women_percentage=0)
                #     for data in nuwakot_data.json()]
                data = nuwakot_data.json()
                with transaction.atomic():
                    for d in data:
                        gaunpalika = d['Municipality']
                        if gaunpalika == "None":
                            continue
                        print(gaunpalika)
                        obj = Data.objects.get(gaunpalika__name=gaunpalika)
                        obj.received_tranche_i = d["received_trache_i"]
                        obj.received_tranche_ii = d["received_trache_ii"]
                        obj.received_tranche_iii = d["received_trache_iii"]

                        obj.houses_in_stage_i = d["house_in_stage_i"]
                        obj.houses_in_stage_ii = d["house_in_stage_ii"]
                        obj.houses_in_stage_iii = d["house_in_stage_iii"]
                        obj.houses_completed = d["houses_completed"]
                        obj.total_houses = d["total_houses"]
                        # print(obj.__dict__)
                        obj.save()
        except Exception as e:
            print(str(e))
            raise CommandError('No data available.')

        self.stdout.write(self.style.SUCCESS('Successfully updated database'))