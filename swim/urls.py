from rest_framework import routers
from .views import SwimmerViewSet

router = routers.DefaultRouter()

router.register('views/swimmer', SwimmerViewSet, 'swimmer')

urlpatterns = router.urls