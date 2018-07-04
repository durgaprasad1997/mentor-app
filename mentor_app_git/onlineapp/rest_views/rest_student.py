from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from onlineapp.models import Student
from onlineapp.rest_views.Serializer import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token
from .rest_auth import *



class StudentList(ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.filter(Colleges__id=self.kwargs['pk']).values()
        return queryset
    def perform_create(self, serializer):
        college=Colleges.objects.get(pk=self.kwargs['pk'])
        serializer.save(Colleges=college)


class StudentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.filter(pk=self.kwargs['pk'])
        return queryset




@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

