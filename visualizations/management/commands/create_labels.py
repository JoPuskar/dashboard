from django.core.management.base import BaseCommand, CommandError

from visualizations.models import ReconstructionGrant, HousingCompletion


class Command(BaseCommand):
    help = 'Create districts in the beginning.'

    def handle(self, *args, **options):
        try:
            housing = ['Houses Completed', 'Houses in Stage I', 'Houses in Stage II', 'Houses in Stage III']
            reconstruction = ['Received Tranche - I', 'Received Tranche - II', 'Received Tranche - III']
            for l in housing:
                HousingCompletion.objects.get_or_create(label=l)
            for r in reconstruction:
                ReconstructionGrant.objects.get_or_create(label=r)
        except:
            CommandError("Command Error!")
        self.stdout.write(self.style.SUCCESS('Successfully Created labels!'))