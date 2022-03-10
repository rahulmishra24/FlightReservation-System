from django.shortcuts import render
from rest_framework import viewsets
from .models import Flights,Reservation
from rest_framework.authtoken.models import Token
from .serializers import FlightSerializers, UserSerializers, ReservationSerializers,EmptySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import status
# Create your views here.


User = get_user_model()

class FeatureViewSet(viewsets.GenericViewSet):
    serializer_class = EmptySerializer
    @action(methods=['POST', ], detail=False)
    def find_flights(self,request):
        city1 = request.data['arrivalCity']
        city2 = request.data['departureCity']
        time = request.data['departureDate']
        flights = Flights.objects.filter(arrivalCity=city1,departureCity=city2,departureDate=time)
        serializers = FlightSerializers(flights,many=True)

        if flights:
            return Response(serializers.data)
        else:
            return Response("No Flight found with these detail")

    
    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def save_reservation(self,request):
        print("hello")
        user = request.user
        flights = Flights.objects.get(id=request.data['flightId'])
        reservation = Reservation() 
        reservation.flight = flights
        reservation.passenger=user
        reservation.save()
        print(reservation.flight.id," ",reservation.passenger.email)
        return Response(status = status.HTTP_201_CREATED)
        

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightSerializers



      
    

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers

