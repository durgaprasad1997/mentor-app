from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onlineapp.models import Marks
from onlineapp.rest_views.Serializer import *



class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['problem1', 'problem2', 'problem3', 'problem4', 'Total']





@api_view(['GET', 'POST'])
def mark_list(request):

    if request.method == 'GET':
        snippets = Marks.objects.values("student_id","id","problem1","problem2","problem3","problem4","Total")


        serializer = MarkSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def mark_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Marks.objects.get(pk=pk)
    except Marks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MarkSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MarkSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

