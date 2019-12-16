from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 童年
from django.http import JsonResponse
from django.core import serializers

from fontapp.models import *

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarShareSerializer, ThirdPartySerializer
from .models import CarShare, ThirdParty
from django.utils.timezone import now

# Create your views here.
class CarShareViewSet(ModelViewSet):
    queryset = CarShare.objects.all()
    serializer_class = CarShareSerializer

class ThirdPartyViewSet(ModelViewSet):
    queryset = ThirdParty.objects.filter(createtime__gt=now().date()).values('content', 'phone')
    serializer_class = ThirdPartySerializer

def index(request):
    return HttpResponse('hell world!')