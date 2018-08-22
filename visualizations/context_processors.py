from .models import ProjectStakeholders


def partners_processor(request):
    partners = ProjectStakeholders.objects.all()

    return {'partners': partners }