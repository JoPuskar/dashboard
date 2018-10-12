from .models import ProjectStakeholders


def partners_processor(request):
    partners = ProjectStakeholders.objects.order_by('project_stakeholders__order')

    return {'partners': partners}