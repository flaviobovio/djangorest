""" Api routes """
from rest_framework import routers
from .api_v1 import SwimmerViewSet, DateViewSet, MarkViewSet

router = routers.DefaultRouter()

router.register('api_v1/swimmer', SwimmerViewSet, 'swimmer')
router.register('api_v1/date', DateViewSet, 'date')
router.register('api_v1/mark', MarkViewSet, 'mark')

urlpatterns = router.urls
