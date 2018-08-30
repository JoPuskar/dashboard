from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Create default groups with permission'

    def handle(self, *args, **options):
        groups_list = ['UNDP Admin', 'UNOPS Admin', 'EOI Admin', 'UNDP Group', 'UNOPS Group', 'EOI Group']

        for group in groups_list:
            group, created = Group.objects.get_or_create(name=group)

            project_stakeholders_perm = ContentType.objects.get(app_label='visualizations', model='projectstakeholders')
            perms = Permission.objects.filter(content_type=project_stakeholders_perm)
            for p in perms:
                group.permissions.add(p)

            training_perm = ContentType.objects.get(app_label='visualizations', model='training')
            perms = Permission.objects.filter(content_type=training_perm)
            for p in perms:
                group.permissions.add(p)

            event_perm = ContentType.objects.get(app_label='visualizations', model='event')
            perms = Permission.objects.filter(content_type=event_perm)
            for p in perms:
                group.permissions.add(p)

            recent_stories_perm = ContentType.objects.get(app_label='visualizations', model='recentstories')
            perms = Permission.objects.filter(content_type=recent_stories_perm)
            for p in perms:
                group.permissions.add(p)

            materials_perm = ContentType.objects.get(app_label='visualizations', model='materials')
            perms = Permission.objects.filter(content_type=materials_perm)
            for p in perms:
                group.permissions.add(p)

            contact_perm = ContentType.objects.get(app_label='visualizations', model='contact')
            perms = Permission.objects.filter(content_type=contact_perm)
            for p in perms:
                group.permissions.add(p)


