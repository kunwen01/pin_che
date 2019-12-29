from django.db import models
from django.utils import timezone

# Create your models here.
class CarShare(models.Model):
    plate = models.CharField(max_length=30)
    start = models.CharField(max_length=90)
    end = models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    phone = models.CharField(max_length=11)
    seat = models.IntegerField()
    number = models.IntegerField()
    mark = models.TextField()
    type = models.IntegerField(default=1) # 1、车找人 2 、人找车
    state = models.IntegerField(default=1) # 1，正常，0删除
    createtime = models.DateTimeField('日期', default=timezone.now)
    def __unicode__(self):
        return self.phone

class ThirdParty(models.Model):
    phone = models.CharField(max_length=120) # list
    content = models.CharField(max_length=120)
    type = models.IntegerField(default=1) # 1、车找人 2 、人找车
    state = models.IntegerField(default=1) # 1，正常，0删除
    createtime = models.DateTimeField('日期', default=timezone.now)
    def __unicode__(self):
        return self.phone

