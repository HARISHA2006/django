# Ex02 Django ORM Web Application
## Date:08.03.2024
## Name: HARISHA.S
## Roll No:212223040063
## DEPT:CSE

## AIM
To develop a Django application to store and retrieve data from a train database using Object Relational Mapping(ORM).

## Entity Relationship Diagram





![web ex 2](https://github.com/HARISHA2006/django/assets/148843830/d364a8e1-00cf-4ea3-b79f-a4b35187d204)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 train

## PROGRAM

admin.py
```
from django.contrib import admin

from .models import Train, TrainAdmin

admin.site.register(Train, TrainAdmin)
```
models.py
```
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

```

## OUTPUT
![alt text](<Screenshot 2024-03-13 051921.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
