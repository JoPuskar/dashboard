from django.urls import path

from . import views

app_name = 'visualizations'

urlpatterns = [
    # path('', views.Dashboard.as_view(), name='dashboard'),
    path('housing-create', views.HousingCompletionCreate.as_view(), name="housing_create"),
    path('reconstruction-create', views.ReconstructionGrantCreate.as_view(), name="reconstruction_create"),
    path('recent-story-create', views.RecentStoryCreate.as_view(), name="recent_story_create"),
    path('housing-update/<int:pk>', views.HousingCompletionUpdate.as_view(), name="housing_update"),
    path('reconstruction-update/<int:pk>', views.ReconstructionGrantUpdate.as_view(), name="reconstruction-update"),
    path('recent-story-update/<int:pk>', views.RecentStoryUpdate.as_view(), name="recent_story_update"),
    path('recent-stories/', views.RecentStoriesView.as_view(), name="recent_stories"),
    path('recent-story-detail/<int:pk>', views.RecentStoryDetail.as_view(), name="recent_story_detail"),
]