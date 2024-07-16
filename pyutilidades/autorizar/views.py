from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class CadastroView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=201)

class LoginView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):
        serializer = AuthTokenSerializer(data=request.data)
        usuario = User.objects.filter(username=request.data['username'])
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        if usuario != []:
            usuario = usuario[0]
            usuario = UsuarioSerializer(usuario)
            return Response(data={'access_token': token.key,'user':usuario.data})
        return Response(data={'access_token': token.key})
