
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .models import HousingCompletion, ReconstructionGrant, RecentStory,\
    District, Gaunpalika, Data
import twitter
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView

from dashboard import settings
from .models import HousingCompletion, ReconstructionGrant, RecentStory



class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_data = {}
        data = Data.objects.all()

        total_houses_completed = 0
        total_houses_stage_i = 0
        total_houses_stage_ii = 0
        total_houses_stage_iii = 0
        total_received_tranche_i = 0
        total_received_tranche_ii = 0
        total_received_tranche_iii = 0

        sum_women_percentage = 0

        gorkha_houses_completed = 0
        gorkha_total_houses_stage_i = 0
        gorkha_total_houses_stage_ii = 0
        gorkha_total_houses_stage_iii = 0
        gorkha_total_received_tranche_i = 0
        gorkha_total_received_tranche_ii = 0
        gorkha_total_received_tranche_iii = 0

        nuwakot_houses_completed = 0
        nuwakot_total_houses_stage_i = 0
        nuwakot_total_houses_stage_ii = 0
        nuwakot_total_houses_stage_iii = 0
        nuwakot_total_received_tranche_i = 0
        nuwakot_total_received_tranche_ii = 0
        nuwakot_total_received_tranche_iii = 0

        for data in data:
            total_houses_completed += data.houses_completed
            total_houses_stage_i += data.houses_in_stage_i
            total_houses_stage_ii += data.houses_in_stage_ii
            total_houses_stage_iii += data.houses_in_stage_iii

            total_received_tranche_i += data.received_tranche_i
            total_received_tranche_ii += data.received_tranche_ii
            total_received_tranche_iii += data.received_tranche_iii

            sum_women_percentage += data.women_percentage

            if data.gaunpalika.district.name == 'Gorkha':
                gorkha_houses_completed += data.houses_completed
                gorkha_total_houses_stage_i += data.houses_in_stage_i
                gorkha_total_houses_stage_ii += data.houses_in_stage_ii
                gorkha_total_houses_stage_iii += data.houses_in_stage_iii

                gorkha_total_received_tranche_i += data.received_tranche_i
                gorkha_total_received_tranche_ii += data.received_tranche_ii
                gorkha_total_received_tranche_iii += data.received_tranche_iii

            if data.gaunpalika.district.name == 'Nuwakot':
                nuwakot_houses_completed += data.houses_completed
                nuwakot_total_houses_stage_i += data.houses_in_stage_i
                nuwakot_total_houses_stage_ii += data.houses_in_stage_ii
                nuwakot_total_houses_stage_iii += data.houses_in_stage_iii

                nuwakot_total_received_tranche_i += data.received_tranche_i
                nuwakot_total_received_tranche_ii += data.received_tranche_ii
                nuwakot_total_received_tranche_iii += data.received_tranche_iii

        all_data['total_houses_completed'] = total_houses_completed
        all_data['total_houses_stage_i'] = total_houses_stage_i
        all_data['total_houses_stage_ii'] = total_houses_stage_ii
        all_data['total_houses_stage_iii'] = total_houses_stage_iii

        all_data['total_received_tranche_i'] = total_received_tranche_i
        all_data['total_received_tranche_ii'] = total_received_tranche_ii
        all_data['total_received_tranche_iii'] = total_received_tranche_iii

        all_data['gorkha_total_houses_completed'] = gorkha_houses_completed
        all_data['gorkha_total_houses_stage_i'] = gorkha_total_houses_stage_i
        all_data['gorkha_total_houses_stage_ii'] = gorkha_total_houses_stage_ii
        all_data['gorkha_total_houses_stage_iii'] = gorkha_total_houses_stage_iii

        all_data['gorkha_total_received_tranche_i'] = gorkha_total_received_tranche_i
        all_data['gorkha_total_received_tranche_ii'] = gorkha_total_received_tranche_ii
        all_data['gorkha_total_received_tranche_iii'] = gorkha_total_received_tranche_iii

        all_data['nuwakot_total_houses_completed'] = nuwakot_houses_completed
        all_data['nuwakot_total_houses_stage_i'] = nuwakot_total_houses_stage_i
        all_data['nuwakot_total_houses_stage_ii'] = nuwakot_total_houses_stage_ii
        all_data['nuwakot_total_houses_stage_iii'] = nuwakot_total_houses_stage_iii

        all_data['nuwakot_total_received_tranche_i'] = nuwakot_total_received_tranche_i
        all_data['nuwakot_total_received_tranche_ii'] = nuwakot_total_received_tranche_ii
        all_data['nuwakot_total_received_tranche_iii'] = nuwakot_total_received_tranche_iii

        context = {'all_data': all_data}

        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['housing_values'] = [total_houses_completed, total_houses_stage_i, total_houses_stage_ii,\
                                     total_houses_stage_iii]

        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['reconstruction_values'] = [total_received_tranche_i, total_received_tranche_ii,\
                                            total_received_tranche_iii]

        context['recent_story'] = RecentStory.objects.all()

        context['district_json_path'] = "/static/json/District.json"
        context['gorkha_json_path'] = "/static/json/Gorkha.json"
        context['nuwakot_json_path'] = "/static/json/Nuwakot.json"

        sum_women_percentage = Data.objects.aggregate(sum_wp=Sum('women_percentage'))
        denom = Data.objects.aggregate(total=Count('women_percentage'))
        denom = denom['total']*100
        if denom:
            context['total_women_percentage'] = round((sum_women_percentage['sum_wp']/denom)*100)

        sum_women_percentage = Data.objects.filter(gaunpalika__district__id=1).aggregate(sum_wp=Sum('women_percentage'))
        denom = Data.objects.filter(gaunpalika__district__id=1).aggregate(total=Count('women_percentage'))
        denom = denom['total']*100
        if denom:
            context['gorkha_women_percentage'] = round((sum_women_percentage['sum_wp']/denom)*100)

        sum_women_percentage = Data.objects.filter(gaunpalika__district__id=2).aggregate(sum_wp=Sum('women_percentage'))
        denom = Data.objects.filter(gaunpalika__district__id=2).aggregate(total=Count('women_percentage'))
        denom = denom['total']*100
        if denom:
            context['nuwakot_women_percentage'] = round((sum_women_percentage['sum_wp']/denom)*100)

        context['data_values_gorkha'] = Data.objects.filter(gaunpalika__district__name='Gorkha').values_list('gaunpalika__name',\
                            'houses_completed', 'houses_in_stage_i',\
                            'houses_in_stage_ii', 'houses_in_stage_iii', 'received_tranche_i',\
                            'received_tranche_ii', 'received_tranche_iii', 'women_percentage')

        context['data_values_nuwakot'] = Data.objects.filter(gaunpalika__district__name='Nuwakot').values_list('gaunpalika__name','houses_completed',\
                            'houses_in_stage_i', 'houses_in_stage_ii', 'houses_in_stage_iii', 'received_tranche_i',\
                            'received_tranche_ii', 'received_tranche_iii', 'women_percentage')

        context['gorkha_data'] = Data.objects.filter(gaunpalika__district__name='Gorkha').values_list('gaunpalika__name')

        context['nuwa_data'] = Data.objects.filter(gaunpalika__district__name='Nuwakot').values_list('gaunpalika__name')
        return context


class HousingCompletionCreate(CreateView):
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class HousingCompletionUpdate(UpdateView):
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class ReconstructionGrantCreate(CreateView):
    model = ReconstructionGrant
    template_name = "visualizations/reconstruction_grant_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class ReconstructionGrantUpdate(UpdateView):
    model = ReconstructionGrant
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class RecentStoryCreate(CreateView):
    model = RecentStory
    template_name = "visualizations/recent_story_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class RecentStoryUpdate(UpdateView):
    model = RecentStory
    template_name = "visualizations/recent_story_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


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



class DataDetail(DetailView):
    model = Data
    template_name = "dashboard.html"
    context_object_name = "data"



def get_posts():
    import facebook
    graph = facebook.GraphAPI(access_token=" 10211098638174413", version="2.12")
    return graph

def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    api = twitter.Api(consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECERET,
                      access_token_key=settings.TOKEN, access_token_secret=settings.TOKEN_SECRET)

    # return api.GetUserTimeline(screen_name='nepalearthquake', exclude_replies=True, include_rts=False)  # includes entities
    return api.GetSearch(term="IndiaInNepal")
    # return api.search.tweets(q='%23hillarysoqualified')

class Dashboard(TemplateView):
    template_name = "visualizations/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['housing_values'] = list(HousingCompletion.objects.values_list('value', flat=True))
        context['reconstruction_values'] = list(ReconstructionGrant.objects.values_list('value', flat=True))
        context['recent_story'] = RecentStory.objects.all()
        context['district_json_path'] = "/static/json/District.json"
        context['gorkha_json_path'] = "/static/json/Gorkha.json"
        context['nuwakot_json_path'] = "/static/json/Nuwakot.json"
        context['tweets'] = get_tweets()
        # import ipdb
        # ipdb.set_trace()
        return context

