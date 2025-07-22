"""  ViewSets """
from rest_framework import viewsets, filters
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



class DateViewSet(viewsets.ModelViewSet):
    """ Date ViewSet """
    # queryset = Date.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = DateSerializer

    def get_queryset(self):
        queryset = Date.objects.all()
        active = self.request.query_params.get('active')

        if active is not None:
            if active.lower() == 'true':
                queryset = queryset.filter(active=True)
            elif active.lower() == 'false':
                queryset = queryset.filter(active=False)
            else:
                raise ValueError("Invalid value for 'active' parameter. Use 'true' or 'false'.")
        return queryset




class MarkViewSet(viewsets.ModelViewSet):
    """ Mark ViewSet """
    queryset = Mark.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MarkSerializer
