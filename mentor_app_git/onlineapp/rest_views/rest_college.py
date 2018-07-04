from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onlineapp.models import Colleges
from onlineapp.rest_views.Serializer import *


from .rest_auth import *




@api_view(['GET', 'POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def college_list(request):


    if request.method == 'GET':
        snippets = Colleges.objects.values("id","Name","Acronym","Location","Contact")
        serializer = CollegeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
def college_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Colleges.objects.get(pk=pk)
    except Colleges.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollegeSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollegeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

