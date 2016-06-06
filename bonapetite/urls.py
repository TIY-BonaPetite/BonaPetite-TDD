from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bpmodels.views import ElectricalConductivityViewSet, TemperatureViewSet

router = routers.DefaultRouter()
router.register(r'^data/ec/', ElectricalConductivityViewSet)
router.register(r'^data/temp/', TemperatureViewSet)

urlpatterns = [
    url(r'^', include('bpmodels.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^api-auth/',
    #     include('rest_framework.urls',
    #             namespace='rest_framework')),
]
