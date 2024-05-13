from rest_framework import viewsets

from streetculture.models import StreetCulture, StreetCultureType
from streetculture.serializers import (StreetCultureSerializer,
                                       StreetCultureTypeSerializer)


class StreetCultureViewSet(viewsets.ModelViewSet):
    """ViewSet для модели StreetCulture"""
    queryset = StreetCulture.objects.all()
    serializer_class = StreetCultureSerializer


class StreetCultureTypeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели StreetCultureType"""
    queryset = StreetCultureType.objects.all()
    serializer_class = StreetCultureTypeSerializer
