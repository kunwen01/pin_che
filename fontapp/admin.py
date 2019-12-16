from django.contrib import admin

# Register your models here.

from fontapp.models import CarShare, ThirdParty

admin.site.register(CarShare)
admin.site.register(ThirdParty)