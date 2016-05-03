from django.db import models

# Create your models here.
from django.db import models


class Humidity(models.Model):
    humity_level = models.FloatField()
    pub_date = models.DateTimeField('date published')


class Temperature(models.Model):
    temperature = models.FloatField()
    pub_date = models.DateTimeField('date published')


class DataCollect(models.Model):
    humidity = models.ForeignKey(Humidity, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)

    location_text = models.CharField(max_length=200)
    #
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)