""" DjangoRest serializers """
from rest_framework import serializers
from .models import Swimmer


class SwimmerSerializer(serializers.ModelSerializer):
    """ Swimmer serializer """
    class Meta:
        """ Swimmer Meta class """
        model = Swimmer
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
