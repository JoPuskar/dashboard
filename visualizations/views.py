from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from .models import HousingCompletion, ReconstructionGrant, RecentStory


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['housing_values'] = list(HousingCompletion.objects.values_list('value', flat=True))
        context['reconstruction_values'] = list(ReconstructionGrant.objects.values_list('value', flat=True))
        context['recent_story'] = RecentStory.objects.all()
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
    model = HousingCompletion
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

