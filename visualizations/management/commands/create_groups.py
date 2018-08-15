from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Create default groups with permission'

    def handle(self, *args, **options):
        staff_group, created = Group.objects.get_or_create(name="Staff")

        contact_perm = ContentType.objects.get(app_label='visualizations', model='contact')
        perms = Permission.objects.filter(content_type=contact_perm)
        for p in perms:
            staff_group.permissions.add(p)

        training_perm = ContentType.objects.get(app_label='visualizations', model='training')
        perms = Permission.objects.filter(content_type=training_perm)
        for p in perms:
            staff_group.permissions.add(p)

        event_perm = ContentType.objects.get(app_label='visualizations', model='event')
        perms = Permission.objects.filter(content_type=event_perm)
        for p in perms:
            staff_group.permissions.add(p)

        recent_stories_perm = ContentType.objects.get(app_label='visualizations', model='recentstories')
        perms = Permission.objects.filter(content_type=recent_stories_perm)
        for p in perms:
            staff_group.permissions.add(p)

