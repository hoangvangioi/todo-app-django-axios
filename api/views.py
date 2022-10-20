from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.


@api_view(['GET'])
def api(request, format=None):
    api_urls = {
        'List View': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.get(id=self.kwargs['pk'])
        return queryset

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message": "Created task successfully!", "details": serializer.data})


@api_view(['POST'])
def taskUpdate(request, pk, format=None):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance = task , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "mobile number updated successfully", "details": serializer.data})
    else:
        return Response({"message": "failed", "details": serializer.errors})


class TaskDestroyAPIView(DestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.get(id=self.kwargs['pk'])
        queryset.delete()
        return queryset