from django.core.management.base import BaseCommand, CommandError

from visualizations.models import District, Gaunpalika, Data


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):

        gorkha_list = ['Aarughat', 'Ajirkot',  'Dharche', 'Gandaki',\
                                   'Gorkha', 'Palungtar', 'Sahid Lakhan', 'Siranchok']

        for gaunpalika in gorkha_list:
            print(gaunpalika)
            gorkha = Gaunpalika.objects.get(name__exact=gaunpalika)
            if not Data.objects.filter(gaunpalika=gorkha).exists():
                Data.objects.create(gaunpalika=gorkha)
            else:
                self.stdout.write(self.style.WARNING('{} Data Already Exists!').format(gaunpalika))

        nuwakot_list =['Belkotgadhi Municipality', 'Bidur Municipality', 'Dupcheshwore', 'Kakani', 'Kispang', 'Likhu',
                           'Meghang', 'Panchakanya', 'Shivapuri', 'Suryagadhi', 'Tadi', 'Tarkeswore']

        for gaunpalika in nuwakot_list:
            print(gaunpalika)
            nuwakot = Gaunpalika.objects.get(name__exact=gaunpalika)
            if not Data.objects.filter(gaunpalika=nuwakot).exists():
                Data.objects.create(gaunpalika=nuwakot)
            else:
                self.stdout.write(self.style.WARNING('{} Data Already Exists!'.format(gaunpalika)))

        self.stdout.write(self.style.SUCCESS('Successfully Initialize Gaunpalika!'))