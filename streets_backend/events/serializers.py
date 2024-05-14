from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Event"""
    class Meta:
        model = Event
        fields = [
            'id', 'name', 'time', 'date', 'place', 'description'
        ]
