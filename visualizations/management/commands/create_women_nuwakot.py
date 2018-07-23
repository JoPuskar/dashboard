from django.core.management.base import BaseCommand, CommandError

from visualizations.models import  Data


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):
        try:
            data = {'Kakani': 3, 'Kispang':13, 'Meghang':8, 'Belkotgadhi Municipality':18, 'Suryagadhi':20, 'Likhu':22, 'Tarkeswore':21, 'Tadi':15, 'Dupcheshwore':18, 'Bidur Municipality':25}
            for k, v in data.items():
                Data.objects.filter(gaunpalika__name=k).update(women_percentage=v)

        except:
            CommandError("Command Error!")
        self.stdout.write(self.style.SUCCESS('Successfully Created labels!'))