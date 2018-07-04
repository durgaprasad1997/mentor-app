from rest_framework import serializers
from onlineapp.models import Colleges
from django.utils.six import BytesIO
from django.test import TestCase
from onlineapp.models import Colleges


class CollegeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=128)
    Location = serializers.CharField(max_length=64)
    Acronym = serializers.CharField(max_length=8)
    Contact = serializers.EmailField()




class UnitTest(TestCase):


    def load(self):
        college1 = Colleges(Name='a', Acronym='a', Location='a', Contact='a')
        college2 = Colleges(Name='a1', Acronym='a1', Location='1a', Contact='a1')
        college3 = Colleges(Name='a11', Acronym='a1', Location='a1', Contact='1a')

    def serialize(self):
        c1=Colleges.objects.values("Name","Location").filter(Name='a')


        a1= "<QuerySet [{'Name': 'a', 'Location': 'a'}]>"


        self.assertEqual(a1,str(c1))






