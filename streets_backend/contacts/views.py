from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    '''Вьюсет для модели Contact'''
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
