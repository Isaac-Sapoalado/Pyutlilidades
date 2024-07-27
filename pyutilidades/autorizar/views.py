from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import status
# Create your views here.

def verificar_token(req,pk):
        token = req.headers['Authorization'][6:]
        user = User.objects.get(pk=pk)
        return token == Token.objects.get(user=user).key

def verificar_user(req,pk):
    try:
        userpk = req.data['user']
        return int(pk)==int(userpk)
    except:
        return Response(data={'body_error':'missing user or pk'}, status=status.HTTP_404_NOT_FOUND)





class CadastroView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

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
            return Response(data={'access_token': token.key,'user':usuario.data},status=status.HTTP_201_CREATED)
        return Response(data={'access_token': token.key},status=status.HTTP_201_CREATED)

class AlteraView(APIView):

    def put(self,request):
        try:
            new_pass = request.data.pop('new_password')
            user = User.objects.get(pk=request.data['pk'])
            if new_pass == user.password or user.password != request.data['password']:
                return Response(data={'detail':'passwords must be differents'},status=status.HTTP_400_BAD_REQUEST)
            request.data['password'] = new_pass
            serializer = UsuarioSerializer(instance=user,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=203)
        except:
            return Response(data={'detail':'"new_password" parameter not found'},status=status.HTTP_404_NOT_FOUND,)
