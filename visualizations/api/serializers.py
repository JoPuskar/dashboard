from rest_framework import serializers
from visualizations.models import Data, Gaunpalika, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name',)


class GaunpalikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gaunpalika
        fields = ('id', 'name', 'district', 'is_municipality',)


class DataSerializers(serializers.ModelSerializer):
    district_name = serializers.CharField(source='gaunpalika.district.name', read_only=True)

    class Meta:
        model = Data
        fields = ('id', 'gaunpalika', 'district_name', 'houses_in_stage_i', 'houses_in_stage_ii', 'houses_in_stage_iii', \
                  'received_tranche_i', 'received_tranche_ii', 'received_tranche_iii',)