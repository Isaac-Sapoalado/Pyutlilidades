from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CitacaoSerializer
from .models import Citacao
from rest_framework.permissions import AllowAny

# Create your views here.

class CitacaoView(APIView):
    
    permission_classes = [AllowAny]

    def random_get():
        from random import randint

        index = randint(0,Citacao.objects.count()-1)
        return index

    def get(self,request):

        cita = Citacao.objects.all()[CitacaoView.random_get()]
        serializer = CitacaoSerializer(cita)
        return Response(data=serializer.data, status=200)
    
    def post(self,request):
        serializer = CitacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

