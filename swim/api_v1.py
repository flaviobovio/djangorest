"""  ViewSets """
from rest_framework import viewsets, permissions
from .models import Swimmer, Date, Mark
from .serializers import SwimmerSerializer, DateSerializer, MarkSerializer




# Create your views here

class SwimmerViewSet(viewsets.ModelViewSet):
    """ Swimmer ViewSet"""
    queryset = Swimmer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SwimmerSerializer

class DateViewSet(viewsets.ModelViewSet):
    """ Date ViewSet """
    queryset = Date.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DateSerializer

class MarkViewSet(viewsets.ModelViewSet):
    """ Mark ViewSet """
    queryset = Mark.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarkSerializer
