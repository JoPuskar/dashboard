from visualizations.models import District, Gaunpalika, Data
from rest_framework import viewsets

from .serializers import DistrictSerializer, GaunpalikaSerializer, DataSerializers


class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class GaunpalikaViewSet(viewsets.ModelViewSet):
    serializer_class = GaunpalikaSerializer
    queryset = Gaunpalika.objects.all()


class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializers
    queryset = Data.objects.all()