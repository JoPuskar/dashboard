
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .models import HousingCompletion, ReconstructionGrant, RecentStory, \
    District, Gaunpalika, Data, RecentStories
import twitter
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView

from dashboard import settings
from .models import HousingCompletion, ReconstructionGrant, RecentStory

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

        dispensed_amount = 0

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

        total_houses = 0
        gorkha_total_houses = 0
        nuwakot_total_houses = 0
        for data in data:
            total_houses_completed += data.houses_completed
            total_houses_stage_i += data.houses_in_stage_i
            total_houses_stage_ii += data.houses_in_stage_ii
            total_houses_stage_iii += data.houses_in_stage_iii

            total_received_tranche_i += data.received_tranche_i
            total_received_tranche_ii += data.received_tranche_ii
            total_received_tranche_iii += data.received_tranche_iii

            total_houses += data.total_houses

            sum_women_percentage += data.women_percentage

            if data.gaunpalika.district.name == 'Gorkha':
                gorkha_total_houses += data.total_houses
                gorkha_houses_completed += data.houses_completed
                gorkha_total_houses_stage_i += data.houses_in_stage_i
                gorkha_total_houses_stage_ii += data.houses_in_stage_ii
                gorkha_total_houses_stage_iii += data.houses_in_stage_iii

                gorkha_total_received_tranche_i += data.received_tranche_i
                gorkha_total_received_tranche_ii += data.received_tranche_ii
                gorkha_total_received_tranche_iii += data.received_tranche_iii

            if data.gaunpalika.district.name == 'Nuwakot':
                nuwakot_total_houses += data.total_houses
                nuwakot_houses_completed += data.houses_completed
                nuwakot_total_houses_stage_i += data.houses_in_stage_i
                nuwakot_total_houses_stage_ii += data.houses_in_stage_ii
                nuwakot_total_houses_stage_iii += data.houses_in_stage_iii

                nuwakot_total_received_tranche_i += data.received_tranche_i
                nuwakot_total_received_tranche_ii += data.received_tranche_ii
                nuwakot_total_received_tranche_iii += data.received_tranche_iii

        dispensed_amount = (total_received_tranche_i  *  50000) + (total_received_tranche_ii * 150000) + (total_received_tranche_iii * 100000)
        progress = (dispensed_amount * 100) / (50000*300000)
        progress = int(progress)

        all_data['total_houses_completed'] = total_houses_completed
        all_data['total_houses_stage_i'] = total_houses_stage_i
        all_data['total_houses_stage_ii'] = total_houses_stage_ii
        all_data['total_houses_stage_iii'] = total_houses_stage_iii

        all_data['total_received_tranche_i'] = total_received_tranche_i
        all_data['total_received_tranche_ii'] = total_received_tranche_ii
        all_data['total_received_tranche_iii'] = total_received_tranche_iii

        all_data['ths1_percentage'] = round((total_houses_stage_i / total_houses) * 100, 2)
        all_data['ths2_percentage'] = round((total_houses_stage_ii / total_houses) * 100, 2)
        all_data['ths3_percentage'] = round((total_houses_stage_iii / total_houses) * 100, 2)

        all_data['trt1_percentage'] = round((total_received_tranche_i / total_houses) * 100, 2)
        all_data['trt2_percentage'] = round((total_received_tranche_ii / total_houses) * 100,
                                                   2)
        all_data['trt3_percentage'] = round((total_received_tranche_iii / total_houses) * 100,
                                                   2)

        all_data['gorkha_total_houses_completed'] = gorkha_houses_completed
        all_data['gorkha_total_houses'] = gorkha_total_houses

        if gorkha_total_houses is not None:
            all_data['gorkha_houses_completed_percentage'] = round((gorkha_houses_completed / gorkha_total_houses) * 100, 2)
            all_data['gorkha_ths1_percentage'] = round((gorkha_total_houses_stage_i/gorkha_total_houses)*100, 2)
            all_data['gorkha_ths2_percentage'] = round((gorkha_total_houses_stage_ii / gorkha_total_houses) * 100, 2)
            all_data['gorkha_ths3_percentage'] = round((gorkha_total_houses_stage_iii / gorkha_total_houses) * 100, 2)
            all_data['gorkha_trt1_percentage'] = round((gorkha_total_received_tranche_i / gorkha_total_houses) * 100, 2)
            all_data['gorkha_trt2_percentage'] = round((gorkha_total_received_tranche_ii / gorkha_total_houses) * 100,
                                                        2)
            all_data['gorkha_trt3_percentage'] = round((gorkha_total_received_tranche_iii / gorkha_total_houses) * 100,
                                                        2)

        all_data['gorkha_total_houses_stage_i'] = gorkha_total_houses_stage_i

        all_data['gorkha_total_houses_stage_ii'] = gorkha_total_houses_stage_ii

        all_data['gorkha_total_houses_stage_iii'] = gorkha_total_houses_stage_iii

        all_data['gorkha_total_received_tranche_i'] = gorkha_total_received_tranche_i

        all_data['gorkha_total_received_tranche_ii'] = gorkha_total_received_tranche_ii
        all_data['gorkha_total_received_tranche_iii'] = gorkha_total_received_tranche_iii

        percentage = round((total_houses_completed / total_houses) * (100), 2)
        all_data['total_houses_completed_percentage'] = percentage

        if nuwakot_total_houses is not None:
            all_data['nuwakot_houses_completed_percentage'] = round(
                (nuwakot_houses_completed / nuwakot_total_houses) * 100, 2)
            all_data['nuwakot_ths1_percentage'] = round((nuwakot_total_houses_stage_i/nuwakot_total_houses)*100, 2)
            all_data['nuwakot_ths2_percentage'] = round((nuwakot_total_houses_stage_ii / nuwakot_total_houses) * 100, 2)
            all_data['nuwakot_ths3_percentage'] = round((nuwakot_total_houses_stage_iii / nuwakot_total_houses) * 100, 2)
            all_data['nuwakot_trt1_percentage'] = round((nuwakot_total_received_tranche_i / nuwakot_total_houses) * 100, 2)
            all_data['nuwakot_trt2_percentage'] = round((nuwakot_total_received_tranche_ii / nuwakot_total_houses) * 100,
                                                        2)
            all_data['nuwakot_trt3_percentage'] = round((nuwakot_total_received_tranche_iii / nuwakot_total_houses) * 100,
                                                        2)

        all_data['nuwakot_total_houses'] = nuwakot_total_houses
        all_data['nuwakot_total_houses_completed'] = nuwakot_houses_completed

        all_data['nuwakot_total_houses_stage_i'] = nuwakot_total_houses_stage_i
        all_data['nuwakot_ths1_percentage'] = round((nuwakot_total_houses_stage_i / nuwakot_total_houses) * 100, 2)

        all_data['nuwakot_total_houses_stage_ii'] = nuwakot_total_houses_stage_ii
        all_data['nuwakot_ths2_percentage'] = round((nuwakot_total_houses_stage_ii / nuwakot_total_houses) * 100, 2)

        all_data['nuwakot_total_houses_stage_iii'] = nuwakot_total_houses_stage_iii
        all_data['nuwakot_ths3_percentage'] = round((nuwakot_total_houses_stage_iii / nuwakot_total_houses) * 100, 2)

        all_data['nuwakot_total_received_tranche_i'] = nuwakot_total_received_tranche_i
        all_data['nuwakot_trt1_percentage'] = round((nuwakot_total_received_tranche_i / nuwakot_total_houses) * 100, 2)

        all_data['nuwakot_total_received_tranche_ii'] = nuwakot_total_received_tranche_ii
        all_data['nuwakot_trt2_percentage'] = round((nuwakot_total_received_tranche_i / nuwakot_total_houses) * 100,
                                                    2)
        all_data['nuwakot_total_received_tranche_iii'] = nuwakot_total_received_tranche_iii
        all_data['nuwakot_trt3_percentage'] = round((nuwakot_total_received_tranche_iii / nuwakot_total_houses) * 100,
                                                    2)

        all_data['total_housess'] = total_houses
        percentage = round((total_houses_completed / total_houses) * (100), 2)
        all_data['total_houses_completed_percentage'] = percentage

        context ['all_data'] = all_data

        context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
        context['housing_values'] = [total_houses_completed, total_houses_stage_i, total_houses_stage_ii, \
                                     total_houses_stage_iii]

        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['reconstruction_values'] = [total_received_tranche_i, total_received_tranche_ii, \
                                            total_received_tranche_iii]

        context['recent_story'] = RecentStories.objects.all()

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

        context['data_values_gorkha'] = Data.objects.filter(gaunpalika__district__name='Gorkha')

        context['data_values_nuwakot'] = Data.objects.filter(gaunpalika__district__name='Nuwakot')

        context['gorkha_data'] = Data.objects.filter(gaunpalika__district__name='Gorkha').values_list('gaunpalika__name')

        context['nuwa_data'] = Data.objects.filter(gaunpalika__district__name='Nuwakot').values_list('gaunpalika__name')
        context['tweets'] = get_tweets()
        context['dispensed_amount'] = dispensed_amount
        context['progress'] = progress
        context['stories'] = RecentStories.objects.all()[:5]
        context['completion_value_gorkha'] = list(Data.objects.filter(gaunpalika__district__name='Gorkha'))
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



# def get_posts():
#     import facebook
#     graph = facebook.GraphAPI(access_token=" 10211098638174413", version="2.12")
#     return graph
#


# class Dashboard(TemplateView):
#     template_name = "visualizations/dashboard.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['housing_label'] = list(HousingCompletion.objects.values_list('label', flat=True))
#         context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
#         context['housing_values'] = list(HousingCompletion.objects.values_list('value', flat=True))
#         context['reconstruction_values'] = list(ReconstructionGrant.objects.values_list('value', flat=True))
#         context['recent_story'] = RecentStory.objects.all()
#         context['district_json_path'] = "/static/json/District.json"
#         context['gorkha_json_path'] = "/static/json/Gorkha.json"
#         context['nuwakot_json_path'] = "/static/json/Nuwakot.json"
#         context['tweets'] = get_tweets()
#         # import ipdb
#         # ipdb.set_trace()
#         return context

