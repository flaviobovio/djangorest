""" DjangoRest serializers """
from rest_framework import serializers
from .models import Category, Club, Swimmer, Date, Mark




class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """
    class Meta:
        """ Category Meta class """
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'Name': {'required': True},
            'age_min': {'required': True}, 
            'age_max': {'required': True},                         
        }

    def validate(self, data):
        age_min = data.get('age_min', self.instance.age_min if self.instance else None)
        age_max = data.get('age_max', self.instance.age_max if self.instance else None)

        # Validate not None
        if age_min is None or age_max is None:
            raise serializers.ValidationError("Both 'age_min' and 'age_max' must be provided and not None")

        # Validate max >= min 
        if age_max < age_min:
            raise serializers.ValidationError("'age_max' must be greater or equal than 'age_min'")

        return data

class ClubSerializer(serializers.ModelSerializer):
    """ Club serializer """
    class Meta:
        """ Club Meta class """
        model = Club
        fields = '__all__'
        extra_kwargs = {
            'Name': {'required': True}
        }



class SwimmerSerializer(serializers.ModelSerializer):
    """ Swimmer serializer """
    # IDs para escritura
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())
    # Detalles anidados para lectura
    club_detail = ClubSerializer(source='club', read_only=True)

    class Meta:
        """ Swimmer Meta class """
        model = Swimmer
        fields = ['id', 'name', 'identification', 'sex','age','club','city','created_at','updated_at', 'club_detail']

        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'age': {'required': True},            
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
    # IDs para escritura
    swimmer = serializers.PrimaryKeyRelatedField(queryset=Swimmer.objects.all())
    date = serializers.PrimaryKeyRelatedField(queryset=Date.objects.all())

    # Detalles anidados para lectura
    swimmer_detail = SwimmerSerializer(source='swimmer', read_only=True)
    date_detail = DateSerializer(source='date', read_only=True)

    class Meta:
        model = Mark
        fields = ['id', 'swimmer', 'date', 'meters', 'swimmer_detail', 'date_detail']

    def validate(self, data):
        """
        Evita marcas duplicadas para un mismo nadador en una misma fecha.
        """
        swimmer = data.get('swimmer')
        date = data.get('date')

        # Si estamos actualizando, excluimos la instancia actual
        instance = self.instance

        if Mark.objects.filter(swimmer=swimmer, date=date).exclude(id=getattr(instance, 'id', None)).exists():
            raise serializers.ValidationError("Ya existe una marca para este nadador en esta fecha.")

        return data