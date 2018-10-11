from visualizations.models import District, Gaunpalika, Data, STFCLocations
from rest_framework import viewsets

from .serializers import DistrictSerializer, GaunpalikaSerializer, DataSerializers
from rest_framework.views import APIView
from django.http import HttpResponse
from django.core.serializers import serialize


class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class GaunpalikaViewSet(viewsets.ModelViewSet):
    serializer_class = GaunpalikaSerializer
    queryset = Gaunpalika.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializers
    queryset = Data.objects.all()


class STFCViewSet(APIView):

    def get(self, request):
    	return HttpResponse(serialize('geojson', STFCLocations.objects.all(),
                                          geometry_field='latlong',
                                          fields=(
                                              'pk',
                                              'district_name',
                                              'name',
                                              'type',
                                              'address',
                                              'contact_number',
                                              'contact_person',
                                          )),
                                content_type='application/json')

