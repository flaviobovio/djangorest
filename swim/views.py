"""  ViewSets """
from rest_framework import viewsets, permissions
from .models import Club, Swimmer, Date, Mark
from .serializers import ClubSerializer, SwimmerSerializer, DateSerializer, MarkSerializer




# Create your views here
class ClubViewSet(viewsets.ModelViewSet):
    """ Club  ViewSet """
    queryset = Club.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClubSerializer    


class SwimmerViewSet(viewsets.ModelViewSet):
    """ Swimmer ViewSet """
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
