from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TodoSerializer
from .models import todo

class TodoList(APIView):
    """
    List all Todo, or create a new Todo.
    """
    def get(self, request, format=None):
        todo_model = todo.objects.all()
        serializer = TodoSerializer(todo_model, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)