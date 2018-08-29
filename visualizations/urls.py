from django.urls import path

from . import views

app_name = 'visualizations'

urlpatterns = [
    # path('', views.Dashboard.as_view(), name='dashboard'),
    path('housing-create', views.HousingCompletionCreate.as_view(), name="housing_create"),
    path('reconstruction-create', views.ReconstructionGrantCreate.as_view(), name="reconstruction_create"),
    path('housing-update/<int:pk>', views.HousingCompletionUpdate.as_view(), name="housing_update"),
    path('reconstruction-update/<int:pk>', views.ReconstructionGrantUpdate.as_view(), name="reconstruction-update"),
    path('recent-stories/', views.RecentStoriesView.as_view(), name="recent_stories"),
    path('recent-story-detail/<int:pk>', views.RecentStoryDetail.as_view(), name="recent_story_detail"),
    path('trainings', views.TrainingListView.as_view(), name="training"),
    path('training-detail/<int:pk>', views.TrainingDetailView.as_view(), name="training_detail"),
    path('contacts', views.ContactListView.as_view(), name="contact"),
    path('materials', views.MaterialsListView.as_view(), name="materials"),
    path('partner-detail/<int:pk>', views.ProjectStakeholdersDetailView.as_view(), name="partner_detail"),
    path('events', views.EventsListView.as_view(), name="event"),
    path('event-detail/<int:pk>', views.EventDetailView.as_view(), name="event_detail"),
    path('about', views.AboutView.as_view(), name="about"),
    path('media', views.MediaView.as_view(), name="media"),

]