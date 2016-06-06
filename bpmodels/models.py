from django.db import models


class ElectricalConductivity(models.Model):
    electrical_conductivity = models.FloatField()
    time_collected = models.DateTimeField(auto_now_add=True)


class Temperature(models.Model):
    temperature = models.FloatField()
    time_collected = models.DateTimeField(auto_now_add=True)
