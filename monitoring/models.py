from django.db import models

# Create your models here.
from django.db import models


class Humidity(models.Model):
    humity_level = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.humity_level


class Temperature(models.Model):
    temperature = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.temperature

class Location(models.Model):
    location = models.CharField(max_length=50)
    location_long_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Record(models.Model):
    humidity = models.ForeignKey(Humidity, on_delete=models.CASCADE)
    temperature = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'Humidity: ' + self.humidity +\
            'Temperature: ' + self.temperature+\
            'Location: ' + self.location+\
            'Date: ' + self.pub_date
