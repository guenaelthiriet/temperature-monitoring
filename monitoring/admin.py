from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Humidity, Temperature, Location, Record

admin.site.register(Humidity)
admin.site.register(Temperature)
admin.site.register(Location)
admin.site.register(Record)