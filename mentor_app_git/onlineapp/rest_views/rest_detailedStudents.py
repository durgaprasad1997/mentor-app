from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onlineapp.models import Marks
from onlineapp.rest_views.Serializer import *


class StudentDetailSerializer(serializers.ModelSerializer):
    mocktest1 = StudentDetailedSerializer()

    class Meta:
        model = Student
        fields = ['id', 'Name', 'dob', 'Email_id', 'Dbname', 'dropped_out', 'Colleges', 'mocktest1']




@api_view(['GET', 'POST'])
def detailedstudents_list(request,id):

    if request.method == 'GET':


        snippets = Student.objects.get(pk=id)
        serializer = StudentDetailedSerializer(snippets)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentDetailedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def detailedstudents_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Marks.objects.get(pk=pk)
    except Marks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentDetailedSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentDetailedSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

