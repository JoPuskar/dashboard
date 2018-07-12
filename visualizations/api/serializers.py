from rest_framework import serializers
from visualizations.models import Data, Gaunpalika, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name', 'gaunpalika',)


class GaunpalikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gaunpalika
        fields = ('id', 'name', 'district', 'is_municipality',)


class DataSerializers(serializers.ModelSerializer):
    gaunpalika_name = serializers.CharField(source='gaunpalika.name', read_only=True)

    class Meta:
        model = Data
        fields = ('gaunpalika_name', 'houses_in_stage_i', 'houses_in_stage_ii', 'houses_in_stage_iii', \
                  'received_tranche_i', 'received_tranche_ii', 'received_tranche_iii',\
                  'total_houses', 'houses_completed', 'women_percentage',)