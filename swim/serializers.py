""" DjangoRest serializers """
from rest_framework import serializers
from .models import Swimmer, Date, Mark


class SwimmerSerializer(serializers.ModelSerializer):
    """ Swimmer serializer """
    class Meta:
        """ Swimmer Meta class """
        model = Swimmer
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True}
        }

class DateSerializer(serializers.ModelSerializer):
    """ Date serializer """
    class Meta:
        """ Date Meta class """
        model = Date
        fields = '__all__'
        extra_kwargs = {
            'date': {'required': True}
        }

class MarkSerializer(serializers.ModelSerializer):
    """ Mark serializer """
    class Meta:
        """ Mark Meta class """
        model = Mark
        fields = '__all__'
        extra_kwargs = {
            'meters': {'required': True}
        }
