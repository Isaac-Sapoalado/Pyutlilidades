from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Palavraserializer,Dicaserializer
from .models import Dica,Palavra
from rest_framework.permissions import AllowAny
# Create your views here.


class Palavraview(APIView):

    permission_classes = [AllowAny]

    def random_get():
        from random import randint

        index = randint(0,Palavra.objects.count()-1)
        return index

    def get(self,request):

        palavra = Palavra.objects.all()[Palavraview.random_get()]
        serializer = Palavraserializer(palavra)
        return Response(data=serializer.data, status=200)