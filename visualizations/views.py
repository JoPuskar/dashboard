from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .models import HousingCompletion, ReconstructionGrant, RecentStory,\
    District, Gaunpalika, Data


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['housing_values'] = list(HousingCompletion.objects.values_list('value', flat=True))

        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['reconstruction_values'] = list(ReconstructionGrant.objects.values_list('value', flat=True))

        context['recent_story'] = RecentStory.objects.all()

        context['district_json_path'] = "/static/json/District.json"
        context['gorkha_json_path'] = "/static/json/Gorkha.json"
        context['nuwakot_json_path'] = "/static/json/Nuwakot.json"

        context['gorkha_total_houses_stage_i'] = Data.objects.filter(gaunpalika__district__id=1).\
                                                aggregate(hs1=Sum('houses_in_stage_i'))
        context['gorkha_total_houses_stage_ii'] = Data.objects.filter(gaunpalika__district__id=1). \
                                                 aggregate(hs2=Sum('houses_in_stage_ii'))
        context['gorkha_total_houses_stage_iii'] = Data.objects.filter(gaunpalika__district__id=1). \
                                                    aggregate(hs3=Sum('houses_in_stage_iii'))

        context['gorkha_total_received_tranche_i'] = Data.objects.filter(gaunpalika__district__id=1).\
                                        aggregate(rt1=Sum('received_tranche_i'))
        context['gorkha_total_received_tranche_ii'] = Data.objects.filter(gaunpalika__district__id=1). \
                                        aggregate(rt2=Sum('received_tranche_ii'))
        context['gorkha_total_received_tranche_iii'] = Data.objects.filter(gaunpalika__district__id=1). \
                                        aggregate(rt3=Sum('received_tranche_iii'))

        context['nuwakot_total_houses_stage_i'] = Data.objects.filter(gaunpalika__district__id=2).\
                                        aggregate(hs1=Sum('houses_in_stage_i'))
        context['nuwakot_total_houses_stage_ii'] = Data.objects.filter(gaunpalika__district__id=2). \
                                        aggregate(hs2=Sum('houses_in_stage_ii'))
        context['nuwakot_total_houses_stage_iii'] = Data.objects.filter(gaunpalika__district__id=2). \
                                        aggregate(hs3=Sum('houses_in_stage_iii'))

        context['nuwakot_total_received_tranche_i'] = Data.objects.filter(gaunpalika__district__id=2).\
                                        aggregate(rt1=Sum('received_tranche_i'))
        context['nuwakot_total_received_tranche_ii'] = Data.objects.filter(gaunpalika__district__id=2). \
                                        aggregate(rt2=Sum('received_tranche_ii'))
        context['nuwakot_total_received_tranche_iii'] = Data.objects.filter(gaunpalika__district__id=2). \
                                        aggregate(rt3=Sum('received_tranche_iii'))
        return context


class HousingCompletionCreate(CreateView):
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class HousingCompletionUpdate(UpdateView):
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class ReconstructionGrantCreate(CreateView):
    model = ReconstructionGrant
    template_name = "visualizations/reconstruction_grant_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class ReconstructionGrantUpdate(UpdateView):
    model = ReconstructionGrant
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class RecentStoryCreate(CreateView):
    model = RecentStory
    template_name = "visualizations/recent_story_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class RecentStoryUpdate(UpdateView):
    model = RecentStory
    template_name = "visualizations/recent_story_create.html"
    fields = '__all__'
    success_url = reverse_lazy("visualizations:dashboard")


class RecentStoryDetail(DetailView):
    model = RecentStory
    template_name = "visualizations/recent_story_detail.html"
    context_object_name = "story"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['housing_values'] = list(HousingCompletion.objects.values_list('value', flat=True))
        context['reconstruction_values'] = list(ReconstructionGrant.objects.values_list('value', flat=True))
        context['recent_story'] = RecentStory.objects.all()
        return context

