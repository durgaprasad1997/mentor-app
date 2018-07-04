from onlineapp.models import Colleges,Student,Marks
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers





class CollegeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=128)
    Location = serializers.CharField(max_length=64)
    Acronym = serializers.CharField(max_length=8)
    Contact = serializers.CharField()

    def create(self, validated_data):
        return Colleges.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Location = validated_data.get('Location', instance.Location)
        instance.Acronym = validated_data.get('Acronym', instance.Acronym)
        instance.Contact = validated_data.get('Contact', instance.Contact)
        instance.save()


        return instance




class StudentSerializer(serializers.Serializer):
    Colleges_id = serializers.IntegerField()
    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=128)
    dob = serializers.CharField(max_length=64)
    Email_id = serializers.EmailField()
    Dbnames = serializers.CharField(max_length=64)
    dropped_out = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('name', instance.Name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.Email_id = validated_data.get('email_id', instance.Email_id)
        instance.Dbnames = validated_data.get('dbnames', instance.Dbnames)
        instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
        instance.Colleges_id = validated_data.get('colleges_id', instance.Colleges_id)
        instance.save()
        return instance



class MarkSerializer(serializers.Serializer):



    student_id=serializers.IntegerField()


    id = serializers.IntegerField(read_only=True)
    problem1 = serializers.IntegerField()
    problem2 = serializers.IntegerField()
    problem3 = serializers.IntegerField()
    problem4 = serializers.IntegerField()
    Total = serializers.IntegerField()


    def create(self, validated_data):
        return Marks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.problem1 = validated_data.get('problem1', instance.problem1)
        instance.problem2 = validated_data.get('problem2', instance.problem2)
        instance.problem3 = validated_data.get('problem3', instance.problem3)
        instance.problem4 = validated_data.get('problem4', instance.problem4)
        instance.Total = validated_data.get('Total', instance.Total)
        instance.save()

        return instance


class StudentDetailedSerializer(serializers.ModelSerializer):

    marks=MarkSerializer()
    class Meta:
        model=Student
        fields=('Colleges_id','id','Name','dob','Email_id','Dbnames','dropped_out','marks')






