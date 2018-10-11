from django.urls import path, include

from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

router.register(r'district', viewset.DistrictViewSet),
router.register(r'gaunpalika', viewset.GaunpalikaViewSet),
router.register(r'data', viewset.DataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('stfc-locations/', viewset.STFCViewSet.as_view(), name="stfc"),

]