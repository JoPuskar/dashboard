from django.core.management.base import BaseCommand, CommandError

from visualizations.models import District, Gaunpalika, Data


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):

        gorkha_list = ['Aarughat', 'Ajirkot', 'Bhimsen', 'Chum Nubri', 'Dharche', 'Gandaki',\
                           'Gorkha', 'Palungtar', 'Sahid Lakhan', 'Siranchok', 'Sulikot']

        for gaunpalika in gorkha_list:
            gorkha = Gaunpalika.objects.get(name__exact=gaunpalika)
            if not Data.objects.filter(gaunpalika=gorkha).exists():
                Data.objects.create(gaunpalika=gorkha)
            else:
                self.stdout.write(self.style.WARNING('{} Data Already Exists!').format(gaunpalika))

        nuwakot_list = ['Belkotgadhi', 'Bidur', 'Dupcheshwar', 'Kakani', 'Kispang', 'Likhu',\
                           'Meghang', 'Panchakanya', 'Shivapuri', 'Suryagadhi', 'Tadi', 'Tarkeshwar']

        for gaunpalika in nuwakot_list:
            nuwakot = Gaunpalika.objects.get(name__exact=gaunpalika)
            if not Data.objects.filter(gaunpalika=nuwakot).exists():
                Data.objects.create(gaunpalika=nuwakot)
            else:
                self.stdout.write(self.style.WARNING('{} Data Already Exists!'.format(gaunpalika)))

        self.stdout.write(self.style.SUCCESS('Successfully Initialize Gaunpalika!'))