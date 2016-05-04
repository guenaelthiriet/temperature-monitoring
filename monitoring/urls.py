from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /monitoring/5/
    url(r'^(?P<record_id>[0-9]+)/$', views.record_detail, name='record_detail'),
    # ex: /monitoring/location/1/
    url(r'^location/(?P<location_id>[0-9]+)/$', views.location_detail, name='location_detail'),
]