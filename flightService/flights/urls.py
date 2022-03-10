from django.urls import path,include
from rest_framework.routers import DefaultRouter
from flights import views
routers = DefaultRouter()
routers.register(r'flights', views.FlightViewSet)
routers.register(r'passenger',views.UserViewSet)
routers.register(r'reservation',views.ReservationViewSet)
routers.register(r'feature', views.FeatureViewSet, basename='auth')
urlpatterns = [
    path('',include(routers.urls)),
    
]