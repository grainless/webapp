from django.contrib.gis import admin
from .models import Chain, Place

admin.site.register(Chain)
admin.site.register(Place, admin.OSMGeoAdmin)
