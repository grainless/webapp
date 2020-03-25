from django.contrib.gis import admin
from places.models import Chain, Place, Review

admin.site.register(Chain)
admin.site.register(Place, admin.OSMGeoAdmin)
admin.site.register(Review)
