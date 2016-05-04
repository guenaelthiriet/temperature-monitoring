from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Record


def index(request):
    latest_records_list = Record.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.__str__() for q in latest_records_list])
    return HttpResponse(output)


def record_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    output = record.__str__()
    return HttpResponse(output)

    return HttpResponse("You're looking at record %s." % record_id)


def location_detail(request, location_id):
    response = "You're looking at the location %s."
    return HttpResponse(response % location_id)