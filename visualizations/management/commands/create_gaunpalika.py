from django.core.management.base import BaseCommand, CommandError

from visualizations.models import District, Gaunpalika


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):

        gorkha_list = ['Aarughat', 'Ajirkot', 'Dharche', 'Gandaki',\
                           'Gorkha', 'Palungtar', 'Sahid Lakhan', 'Siranchok']

        for gaunpalika in gorkha_list:
            gorkha = District.objects.get(name__exact='Gorkha')
            if not Gaunpalika.objects.filter(name=gaunpalika).exists():
                if gaunpalika == 'Gorkha' or gaunpalika == 'Palungtar':
                    Gaunpalika.objects.create(district=gorkha, name=gaunpalika, is_municipality=True)
                else:
                    Gaunpalika.objects.create(district=gorkha, name=gaunpalika)
            else:
                self.stdout.write(self.style.WARNING('{} Gaunpalika Already Exists!').format(gaunpalika))

        nuwakot_list = ['Belkotgadhi Municipality', 'Bidur Municipality', 'Dupcheshwore', 'Kakani', 'Kispang', 'Likhu',\
                           'Meghang', 'Panchakanya', 'Shivapuri', 'Suryagadhi', 'Tadi', 'Tarkeswore']

        for gaunpalika in nuwakot_list:
            nuwakot = District.objects.get(name__exact='Nuwakot')
            if not Gaunpalika.objects.filter(name=gaunpalika).exists():
                if gaunpalika == 'Belkotgadhi Municipality' or gaunpalika == 'Bidur Municipality':
                    Gaunpalika.objects.create(district=nuwakot, name=gaunpalika, is_municipality=True)
                else:
                    Gaunpalika.objects.create(district=nuwakot, name=gaunpalika)
            else:
                self.stdout.write(self.style.WARNING('{} Gaunpalika Already Exists!'.format(gaunpalika)))

        self.stdout.write(self.style.SUCCESS('Successfully Created Gaunpalika!'))