from rest_framework import routers
from .views import SwimmerViewSet, DateViewSet, MarkViewSet

router = routers.DefaultRouter()

router.register('views/swimmer', SwimmerViewSet, 'swimmer')
router.register('views/date', DateViewSet, 'date')
router.register('views/mark', MarkViewSet, 'mark')


urlpatterns = router.urls