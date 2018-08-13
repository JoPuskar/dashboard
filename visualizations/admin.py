from django.contrib import admin

from visualizations.models import HousingCompletion, ReconstructionGrant, RecentStories,\
    District, Gaunpalika, Data, Contact, Training, Event, Media, ProjectStakeholders, DispensedAmount, AboutUs

admin.site.site_header = 'EOI'
admin.site.index_title = 'EOI CMS'


class DataAdmin(admin.ModelAdmin):
    list_display = ['gaunpalika', 'houses_in_stage_i', 'houses_in_stage_ii', 'houses_in_stage_iii', 'received_tranche_i',
                    'received_tranche_ii', 'received_tranche_iii', 'version', 'source_is_fieldSight', 'total_houses', 'houses_completed',
                    'women_percentage']


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'created_by', 'created', 'updated']
    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['partner_name', 'address', 'email', 'website', 'phone', 'logo']


class RecentStoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'thumbnail', 'banner']


class GaunpalikaAdmin(admin.ModelAdmin):
    list_display = ['district', 'name', 'is_municipality']


class HousingCompletionAdmin(admin.ModelAdmin):
    list_display = ['label', 'value']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


admin.site.register(HousingCompletion, HousingCompletionAdmin)
admin.site.register(ReconstructionGrant)
admin.site.register(District)
admin.site.register(Gaunpalika, GaunpalikaAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(RecentStories, RecentStoriesAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Media)
admin.site.register(ProjectStakeholders)
admin.site.register(DispensedAmount)
admin.site.register(AboutUs)


