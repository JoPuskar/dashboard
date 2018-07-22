import requests

from django.core.management.base import BaseCommand, CommandError

from visualizations.models import Data, Gaunpalika, District

gorkha_data = requests.get('http://rims.southeastasia.cloudapp.azure.com:8085/dataForNaxa')

nuwakot_data = requests.get('https://app.fieldsight.org/fieldsight/api/municipality/')


class Command(BaseCommand):
    help = 'Synchronizes the database with data coming from the api.'

    def handle(self, *args, **options):
        try:
            if gorkha_data.json() and False:
                # print(gorkha_data.json())
                [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                    houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                    houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                    received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                    total_houses=data['total_houses'], women_percentage=round(float(data['women_percentage'])), source_is_fieldSight=False)
                    for data in gorkha_data.json()]

            if nuwakot_data.json():
                # print(nuwakot_data.json())
                # [Data.objects.filter(gaunpalika__name=data['Municipality']).update( \
                #     houses_in_stage_i=data['house_in_stage_i'], houses_in_stage_ii=data['house_in_stage_ii'], \
                #     houses_in_stage_iii=data['house_in_stage_iii'], received_tranche_i=data['received_trache_i'], \
                #     received_tranche_ii=data['received_trache_ii'], received_tranche_iii=data['received_trache_iii'], \
                #     total_houses=data['total_houses'], houses_completed=data['houses_completed'], women_percentage=0,)
                #     for data in nuwakot_data.json()[0]]
                Gaunpalika.objects.all().delete()
                district = District.objects.get(name="Nuwakot")
                for municipality in nuwakot_data.json():
                    if municipality["Municipality"] == 'None':
                        # print(municipality["Municipality"], "nonewwwwwww")
                        continue
                    else:
                        print(municipality["Municipality"])
                        gaupalika, true = Gaunpalika.objects.get_or_create(name=municipality["Municipality"], district=district)
                        municipality.pop("Municipality")
                        received_trache_i = municipality.pop("received_trache_i")
                        received_trache_ii = municipality.pop("received_trache_ii")
                        received_trache_iii = municipality.pop("received_trache_iii")

                        houses_in_stage_i = municipality.pop("house_in_stage_i")
                        houses_in_stage_ii = municipality.pop("house_in_stage_ii")
                        houses_in_stage_iii = municipality.pop("house_in_stage_iii")
                        data = Data(received_tranche_i=received_trache_i, received_tranche_ii= received_trache_ii, received_tranche_iii=received_trache_iii,
                                    houses_in_stage_i=houses_in_stage_i, houses_in_stage_ii=houses_in_stage_ii, houses_in_stage_iii=houses_in_stage_iii, gaunpalika=gaupalika)
                        data.save()
                        print(gaupalika.name)
                        print(data.id)
        except Exception as e:
            print(str(e))
            raise CommandError('No data available.')

        self.stdout.write(self.style.SUCCESS('Successfully updated database'))