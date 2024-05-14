from rest_framework import viewsets
from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Event"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
