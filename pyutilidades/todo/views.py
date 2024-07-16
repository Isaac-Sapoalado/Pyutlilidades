from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Tarefa_serializer,Tarefa
from django.http import Http404
from rest_framework import status

# Create your views here.


class Tarefa_View(APIView):

    def get(self,request):
        tarefas = Tarefa.objects.all()
        serializer = Tarefa_serializer(tarefas, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer = Tarefa_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)

class Detail_Tarefa_View(APIView):
    
    def get_object(self, pk):
        try:
            tarefa = Tarefa.objects.filter(user=pk)
            return tarefa
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = Tarefa_serializer(instance=tarefa,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = Tarefa_serializer(instance=tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)