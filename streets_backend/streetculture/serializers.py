from rest_framework import serializers

from streetculture.models import StreetCulture, StreetCultureType


class StreetCultureTypeSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели StreetCultureType'''
    class Meta:
        model = StreetCultureType
        fields = ['name']


class StreetCultureSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели StreetCulture'''
    culture_type = StreetCultureTypeSerializer(read_only=True)

    class Meta:
        model = StreetCulture
        fields = [
            'name', 'description', 'photo', 'video', 'culture_type'
        ]
