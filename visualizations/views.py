import twitter
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from dashboard import settings
from .models import HousingCompletion, ReconstructionGrant, Data, RecentStories, Event, Contact, Training, \
    Media, ProjectStakeholders, DispensedAmount, AboutUs, TotalAmount, Materials, OtherContact


def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    api = twitter.Api(consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECERET,
                      access_token_key=settings.TOKEN, access_token_secret=settings.TOKEN_SECRET)
    # api= 'helo'
    # return api.GetUserTimeline(screen_name='nepalearthquake', exclude_replies=True, include_rts=False)  # includes entities
    return api.GetSearch(term="IndiaInNepalReconstruction")

    # return api


class Dashboard(TemplateView):
    """ TemplateView for Dashboard"""

    template_name = "visualizations/dashboard.html"

    def get_context_data(self, **kwargs):
        """
        :returns total houses, houses completed, houses in stage i, ii & iii, receieved tranche i, ii & iii, women
        percentage, district json path and other context values
        """
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

        dispensed_amount_obj = DispensedAmount.objects.all()[0]
        dispensed_amount = dispensed_amount_obj.amount
        total_amount_obj = TotalAmount.objects.all()[0]
        progress = (dispensed_amount * 100) / total_amount_obj.amount
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
        context['housing_values'] = [total_houses_completed, total_houses_stage_i, total_houses_stage_ii, total_houses_stage_iii]

        context['reconstruction_label'] = list(ReconstructionGrant.objects.values_list('label', flat=True))
        context['reconstruction_values'] = [total_received_tranche_i, total_received_tranche_ii, \
                                            total_received_tranche_iii]

        context['recent_story'] = RecentStories.objects.order_by('-updated')

        context['district_json_path'] = "/static/json/gorkhaNuwakot.json"
        context['district_nepal'] = "/static/json/District.json"
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
        context['stories'] = RecentStories.objects.order_by('-updated')[:5]
        context['project_stakeholders'] = ProjectStakeholders.objects.order_by('project_stakeholders__order')

        return context


class HousingCompletionCreate(CreateView):
    """
    CreateView HousingCompletion
    """
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class HousingCompletionUpdate(UpdateView):
    """
    UpdateView for HousingCompletion
    """
    model = HousingCompletion
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class ReconstructionGrantCreate(CreateView):
    """
    CreateView for ReconstructionGrant
    """

    model = ReconstructionGrant
    template_name = "visualizations/reconstruction_grant_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class ReconstructionGrantUpdate(UpdateView):
    """
    UpdateView for ReconstructionGrant
    """

    model = ReconstructionGrant
    template_name = "visualizations/housing_completion_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class RecentStoryDetail(DetailView):
    """
    DetailView for RecentStories
    """

    model = RecentStories
    template_name = "visualizations/story_detail.html"
    context_object_name = "story"


class DataDetail(DetailView):
    """
    DetailView for DataDetail
    """

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


class RecentStoriesView(ListView):
    """
    ListView for RecentStories
    """

    model = RecentStories
    template_name = "visualizations/stories.html"

    def get_queryset(self):
        return RecentStories.objects.order_by('-updated')


class EventsListView(ListView):
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.order_by('-event_date')


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class TrainingListView(ListView):
    model = Training
    context_object_name = 'trainings'


class TrainingDetailView(DetailView):
    model = Training
    context_object_name = 'training'


class ContactListView(TemplateView):
    context_object_name = 'contacts'
    template_name = 'visualizations/contact_list.html'

    # def get_queryset(self):
    #     return Contact.objects.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.order_by('order')
        context['other_contacts'] = OtherContact.objects.order_by('-pk')
       
        return context



class AboutView(ListView):
    model = AboutUs
    template_name = 'visualizations/about.html'
    context_object_name = 'about'


class MediaView(ListView):
    model = Media

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_list'] = Media.objects.all().order_by('-updated')
        context['audios'] = Media.objects.filter(category='AUDIO').order_by('-updated')
        context['videos'] = Media.objects.filter(category='VIDEO').order_by('-updated')
        context['images'] = Media.objects.filter(category='IMAGE').order_by('-updated')

        return context


class MaterialsListView(ListView):
    model = Materials
    context_object_name = 'materials'


class ProjectStakeholdersDetailView(DetailView):
    model = ProjectStakeholders
    template_name = 'visualizations/project_stakeholders_detail.html'
    context_object_name = 'project_stakeholder'

