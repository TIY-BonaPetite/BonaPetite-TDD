import csv
from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (ElectricalConductivitySerializer,
                          TemperatureSerializer)
from .models import ElectricalConductivity, Temperature


def index(request):
    return render(request, 'index.html')


def sensor_data(request):
    ec_data = ElectricalConductivity.objects.all().order_by('-time_collected')
    temp_data = Temperature.objects.all().order_by('-time_collected')
    context = {'ec_data': ec_data, 'temp_data': temp_data}
    return render(request, 'plantinfo.html', context)


# def electrical_conductivity(request):
#     data = ElectricalConductivity.objects.all().order_by('-time_collected')
#     context = {'data': data, }
#     return render(request, 'plantinfo.html', context)
#
#
# def temperature(request):
#     data = Temperature.objects.all().order_by('-time_collected')
#     context = {'data': data, }
#     return render(request, 'plantinfo.html', context)


# class DataViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows data to be viewed or edited.
#     """
#     queryset = list(chain(
#             ElectricalConductivity.objects.all().order_by('-time_collected'),
#             Temperature.objects.all().order_by('-time_collected')))
#     serializer_class = DataSerializer(queryset, many=True)


class ElectricalConductivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conductivity data to be viewed or edited.
    """
    queryset = ElectricalConductivity.objects.all().order_by('-pH_level')
    serializer_class = ElectricalConductivitySerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows temperature data to be viewed or edited.
    """
    queryset = Temperature.objects.all().order_by('-pH_level')
    serializer_class = TemperatureSerializer


def data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data_csv.csv"'
    writer = csv.writer(response)
    for data in list(chain(ElectricalConductivity.objects.all(),
                           Temperature.objects.all())):
        writer.writerow([data.electrical_conductivity, data.temperature])
    return response
