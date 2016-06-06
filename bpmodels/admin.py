from django.contrib import admin
from .models import ElectricalConductivity, Temperature


class ElectricalConductivityAdmin(admin.ModelAdmin):
    readonly_fields = ('time_collected', )


class TemperatureAdmin(admin.ModelAdmin):
    readonly_fields = ('time_collected', )


admin.site.register(ElectricalConductivity,
                    Temperature,
                    ElectricalConductivityAdmin,
                    TemperatureAdmin)
