
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onlineapp.models import Marks
from onlineapp.rest_views.Serializer import *



@api_view(['GET', 'POST'])
def detailedstudents_list(request,id1,id2):

    if request.method == 'GET':


        snippets = Student.objects.get(pk=id2,Colleges_id=id1)
        serializer = StudentSerializer(snippets)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

