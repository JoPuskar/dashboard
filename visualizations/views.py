from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from .models import HousingCompletion, ReconstructionGrant, RecentStory


class Dashboard(TemplateView):
    template_name = "dashboard.html"


class HousingCompletionCreate(CreateView):
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"


class ReconstructionGrantCreate(CreateView):
    model = ReconstructionGrant
    template_name = "visualizations/reconstruction_grant_create.html"


class RecentStoryCreate(CreateView):
    model = RecentStory
    template_name = "visualizations/recent_story_create.html"
