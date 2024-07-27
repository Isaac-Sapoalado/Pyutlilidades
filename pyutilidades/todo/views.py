from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializer import Tarefa_serializer,Tarefa
from django.http import Http404
from rest_framework import status
from autorizar.views import verificar_token,verificar_user

# Create your views here.


class Tarefa_View(APIView):

    def get(self,request):
        tarefas = Tarefa.objects.all()
        serializer = Tarefa_serializer(tarefas, many=True)
        return Response(serializer.data, status=200)

class Detail_Tarefa_View(APIView):      

    def get_object(self, pk):
        try:
            tarefa = Tarefa.objects.filter(user=pk)
            return tarefa
        except Tarefa.DoesNotExist:
            raise Http404

    def post(self,request,pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            serializer = Tarefa_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(data={'token_error':'invalid token'}, status=401)

    def get(self, request, pk):
        if verificar_token(request,pk=pk):
            tarefa = self.get_object(pk)
            serializer = Tarefa_serializer(instance=tarefa,many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'token_error':'invalid token'}, status=401)

    def delete(self, request, pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            tarefa = Tarefa.objects.get(pk=request.data['pk'])
            tarefa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'token_error':'invalid token'}, status=401)

    def put(self, request, pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            tarefa = Tarefa.objects.get(pk=request.data['pk'])
            serializer = Tarefa_serializer(instance=tarefa, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response(data={'token_error':'invalid token'}, status=401)