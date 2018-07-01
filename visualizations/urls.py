from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('housing-create', views.HousingCompletionCreate.as_view(), name="housing_create"),
    path('reconstruction-create', views.ReconstructionGrantCreate.as_view(), name="reconstruction_create"),
    path('recent-story-create', views.RecentStoryCreate.as_view(), name="recent_story_create"),
]