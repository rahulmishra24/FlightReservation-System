
from rest_framework import serializers
from .models import Flights,Reservation,User

class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'
        

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','last_login','is_superuser','is_active','date_joined','groups','user_permissions','is_staff')

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields ='__all__'

class EmptySerializer(serializers.Serializer):
    pass