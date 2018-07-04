from django.test import TestCase
from rest_framework import serializers
from onlineapp.models import Colleges
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
# Create your tests here.


class CollegeSerializer(serializers.Serializer):

    Name = serializers.CharField(max_length=128)
    Location = serializers.CharField(max_length=64)
    Acronym = serializers.CharField(max_length=8)
    Contact = serializers.EmailField()



class CollegeTestCase(TestCase):

    def setUp(self):
        self.colleges = Colleges.objects.create(Name="lion", Location="roar", Acronym='cbj', Contact='nk@gmail.com')
        self.college_serializer = CollegeSerializer(self.colleges)

    def test_college_valid_serialize(self):
        self.assertEqual(self.college_serializer.data,
                         {'Name': "lion", 'Location': "roar", 'Acronym': 'cbj', 'Contact': 'nk@gmail.com'})

    def test_college_invalid_serialize(self):
        self.assertNotEqual(self.college_serializer.data,
                            {'Name': "lion1", 'Location': "roar", 'Acronym': 'cbj', 'Contact': 'nk@gmail.com'})


    def test_post_college(self):
        self.assertEqual(True)
