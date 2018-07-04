from rest_framework import serializers
from onlineapp.models import Colleges
from django.utils.six import BytesIO

class CollegeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=128)
    Location = serializers.CharField(max_length=64)
    Acronym = serializers.CharField(max_length=8)
    Contact = serializers.EmailField()


