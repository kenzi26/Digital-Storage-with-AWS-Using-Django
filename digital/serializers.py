from rest_framework import serializers
from .models import DigitalStorage


class DigitalStorageSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = DigitalStorage
        fields= '__all__'