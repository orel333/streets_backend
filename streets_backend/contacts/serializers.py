from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'name', 'inn', 'ogrn', 'legal_address', 
            'actual_address', 'email', 'phone'
        ]
