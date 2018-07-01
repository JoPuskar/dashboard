from django.contrib import admin

# Register your models here.
from visualizations.models import HousingCompletion, ReconstructionGrant, RecentStory
admin.site.register(HousingCompletion)
admin.site.register(ReconstructionGrant)
admin.site.register(RecentStory)
