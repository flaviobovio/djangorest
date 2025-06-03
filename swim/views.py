"""  ViewSets """
from rest_framework import viewsets
from .models import Club, Swimmer, Date, Mark, Category
from .serializers import ClubSerializer, SwimmerSerializer, DateSerializer, MarkSerializer, CategorySerializer
from rest_framework import permissions


# Create your views here
class CategoryViewSet(viewsets.ModelViewSet):
    """ Category ViewSet """
    queryset = Category.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = CategorySerializer    

class ClubViewSet(viewsets.ModelViewSet):
    """ Club  ViewSet """
    queryset = Club.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = ClubSerializer    


class SwimmerViewSet(viewsets.ModelViewSet):
    """ Swimmer ViewSet """
    queryset = Swimmer.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SwimmerSerializer

class DateViewSet(viewsets.ModelViewSet):
    """ Date ViewSet """
    queryset = Date.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = DateSerializer

class MarkViewSet(viewsets.ModelViewSet):
    """ Mark ViewSet """
    queryset = Mark.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MarkSerializer
