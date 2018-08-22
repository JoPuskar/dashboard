from .models import ProjectStakeholders


def partners_processor(request):
    partners = ProjectStakeholders.objects.order_by('-updated')

    return {'partners': partners}