from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url, include
from .views import InvestorsViewSet
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView

router = DefaultRouter()
# Endpoint to fetch the all the pitches 

router.register("", InvestorsViewSet, basename="investors")

urlpatterns = [

# Endpoint to specify a particular id (identifying the pitch) to fetch a single Pitch

    path(r'pitches/<m>/',views.get_query),

#Endpoint to post a pitch to the backend

    url('pitches', include(router.urls)),

# Endpoint to make a counter offer for a pitch to the backend

    path('pitches/<id>/makeOffer',views.makeOffer)
]




# router.register(r"/(?P<m>\d+)", InvestorsView, basename="investor")