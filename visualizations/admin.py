from django.contrib import admin
from django.db.models import Q
from visualizations.models import HousingCompletion, ReconstructionGrant, RecentStories,\
    District, Gaunpalika, Data, Contact, Training, Event, Media, ProjectStakeholders, DispensedAmount, AboutUs, TotalAmount, Materials

admin.site.site_header = 'EOI'
admin.site.index_title = 'EOI CMS'


class DataAdmin(admin.ModelAdmin):
    list_display = ['gaunpalika', 'houses_in_stage_i', 'houses_in_stage_ii', 'houses_in_stage_iii', 'received_tranche_i',
                    'received_tranche_ii', 'received_tranche_iii', 'version', 'source_is_fieldSight', 'total_houses', 'houses_completed',
                    'women_percentage']


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by', 'created', 'updated']
    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Admin':
                qs = qs.filter(Q(created_by__groups__name="EOI Group") | Q(created_by__groups__name="EOI Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Admin':
                qs = qs.filter(Q(created_by__groups__name="UNDP Group") | Q(created_by__groups__name="UNDP Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Admin':
                qs = qs.filter(Q(created_by__groups__name="UNOPS Group") | Q(created_by__groups__name="UNOPS Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Group':
                qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class ContactAdminInline(admin.StackedInline):
    model = Contact


class RecentStoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'thumbnail', 'banner']

    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(RecentStoriesAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Admin':
                qs = qs.filter(Q(created_by__groups__name="EOI Group") | Q(created_by__groups__name="EOI Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Admin':
                qs = qs.filter(Q(created_by__groups__name="UNDP Group") | Q(created_by__groups__name="UNDP Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Admin':
                qs = qs.filter(Q(created_by__groups__name="UNOPS Group") | Q(created_by__groups__name="UNOPS Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Group':
                qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class GaunpalikaAdmin(admin.ModelAdmin):
    list_display = ['district', 'name', 'is_municipality']


class HousingCompletionAdmin(admin.ModelAdmin):
    list_display = ['label', 'value']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']

    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(TrainingAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Admin':
                qs = qs.filter(Q(created_by__groups__name="EOI Group") | Q(created_by__groups__name="EOI Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Admin':
                qs = qs.filter(Q(created_by__groups__name="UNDP Group") | Q(created_by__groups__name="UNDP Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Admin':
                qs = qs.filter(Q(created_by__groups__name="UNOPS Group") | Q(created_by__groups__name="UNOPS Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Group':
                qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class ProjectStakeholdersAdmin(admin.ModelAdmin):
    inlines = [ContactAdminInline]

    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(ProjectStakeholdersAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Admin':
                qs = qs.filter(Q(created_by__groups__name="EOI Group") | Q(created_by__groups__name="EOI Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Admin':
                qs = qs.filter(Q(created_by__groups__name="UNDP Group") | Q(created_by__groups__name="UNDP Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Admin':
                qs = qs.filter(Q(created_by__groups__name="UNOPS Group") | Q(created_by__groups__name="UNOPS Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Group':
                qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class MaterialsAdmin(admin.ModelAdmin):

    exclude = ('created_by',)

    def get_queryset(self, request):
        qs = super(MaterialsAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Admin':
                qs = qs.filter(Q(created_by__groups__name="EOI Group") | Q(created_by__groups__name="EOI Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'EOI Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Admin':
                qs = qs.filter(Q(created_by__groups__name="UNDP Group") | Q(created_by__groups__name="UNDP Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNDP Group':
                qs = qs.filter(created_by=request.user)

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Admin':
                qs = qs.filter(Q(created_by__groups__name="UNOPS Group") | Q(created_by__groups__name="UNOPS Admin"))

            if request.user.groups.values_list('name', flat=True)[0] == 'UNOPS Group':
                qs = qs.filter(created_by=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class AboutUsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return AboutUs.objects.all().count() == 0


class DispensedAmountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return DispensedAmount.objects.all().count() == 0


class TotalAmountAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return TotalAmount.objects.all().count() == 0


admin.site.register(HousingCompletion, HousingCompletionAdmin)
admin.site.register(ReconstructionGrant)
admin.site.register(District)
admin.site.register(Gaunpalika, GaunpalikaAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(RecentStories, RecentStoriesAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Media)
admin.site.register(ProjectStakeholders, ProjectStakeholdersAdmin)
admin.site.register(DispensedAmount, DispensedAmountAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(TotalAmount, TotalAmountAdmin)
admin.site.register(Materials, MaterialsAdmin)