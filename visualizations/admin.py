from django.contrib import admin

# Register your models here.
from visualizations.models import HousingCompletion, ReconstructionGrant, RecentStory,\
    District, Gaunpalika, Data

admin.site.register(HousingCompletion)
admin.site.register(ReconstructionGrant)
admin.site.register(RecentStory)
admin.site.register(District)
admin.site.register(Gaunpalika)
admin.site.register(Data)
