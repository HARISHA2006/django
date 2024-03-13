from django.db import models
from django.contrib import admin

class Train(models.Model):
    train_code = models.CharField(max_length=20)
    train_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_station_code = models.CharField(max_length=20)
    end_station_code = models.CharField(max_length=20)

class TrainAdmin(admin.ModelAdmin):
    list_display=('train_code','train_name','start_time','end_time','start_station_code','end_station_code')

