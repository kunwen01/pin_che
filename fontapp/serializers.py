#!/usr/bin/env python
#-*- coding:utf-8 -*-

from rest_framework import serializers
from fontapp.models import CarShare, ThirdParty

class CarShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShare
        fields = '__all__'

class ThirdPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdParty
        fields = '__all__'