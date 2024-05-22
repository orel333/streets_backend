from django.contrib import admin
from events.models import Event, Coordinates, EventLocation

admin.site.register(Event)
admin.site.register(EventLocation)
admin.site.register(Coordinates)
