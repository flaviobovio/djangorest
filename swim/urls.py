""" Api routes """
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import SwimmerViewSet, DateViewSet, MarkViewSet, ClubViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('club', ClubViewSet, 'club')
router.register('swimmer', SwimmerViewSet, 'swimmer')
router.register('date', DateViewSet, 'date')
router.register('mark', MarkViewSet, 'mark')

urlpatterns = [
    path('', include(router.urls)),  
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Swim API'))
]
