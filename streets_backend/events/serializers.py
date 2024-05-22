from rest_framework import serializers
from .models import Coordinates, EventLocation, Event


class CoordinatesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Coordinates"""
    class Meta:
        model = Coordinates
        fields = ['latitude', 'longitude']


class EventLocationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели EventLocation"""
    coordinates = CoordinatesSerializer(read_only=True)
    
    class Meta:
        model = EventLocation
        fields = ['name', 'description', 'address', 'coordinates']


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Event"""
    place = EventLocationSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'name', 'time', 'date', 'place', 'description']
