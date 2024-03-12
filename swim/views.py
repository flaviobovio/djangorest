"""  ViewSets """
from rest_framework import viewsets, permissions
from .models import Swimmer
from .serializers import SwimmerSerializer


# Create your views here

class SwimmerViewSet(viewsets.ModelViewSet):
    queryset = Swimmer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SwimmerSerializer

