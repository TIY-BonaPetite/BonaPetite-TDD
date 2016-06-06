from rest_framework import serializers
from .models import ElectricalConductivity, Temperature


class ElectricalConductivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElectricalConductivity
        fields = '__all__'


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
