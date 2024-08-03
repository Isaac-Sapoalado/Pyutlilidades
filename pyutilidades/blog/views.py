from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from autorizar.views import verificar_token,verificar_user
from .models import Blog,TagBlog,Comentario,Interacao,Tag
from .serializer import Blog_serializer,Interacao_serializer,Comentario_serializer,TagBlog_serializer,Tag_serializer
from rest_framework.permissions import AllowAny
# Create your views here.


class BlogView(APIView):

    def get(self,request,pk):

        if verificar_token(request,pk=pk):
            blog = Blog.objects.filter(user=pk)
            serializer = Blog_serializer(blog,many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self,request,pk):
            
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            serializer = Blog_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):

        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            blog = Blog.objects.get(pk=request.data['pk'])
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            blog = Blog.objects.get(pk=request.data['pk'])
            serializer = Blog_serializer(instance=blog,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
class AllBlogView(APIView):

    permission_classes = [AllowAny]
    
    def get(self,request):

        blogs = Blog.objects.all()
        serializer = Blog_serializer(blogs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class TagView(APIView):

    def get(self,request):
        tags = Tag.objects.all()
        serializer = Tag_serializer(tags,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class TagBlogView(APIView):

    def post(self,request):

        serializer = TagBlog_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class ComentarioView(APIView):
    
    def get(self,request,pk):
        comentario = Comentario.objects.filter(blog=pk)
        serializer = Comentario_serializer(comentario,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            serializer = Comentario_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            comentario = Comentario.objects.get(pk=request.data['pk'],user=pk)
            comentario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

class InteracaoView(APIView):
    
    def get(self,request,pk):
        interacao = Interacao.objects.filter(blog=pk)
        serializer = Interacao_serializer(interacao,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            serializer = Interacao_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if verificar_token(request,pk=pk) and verificar_user(request,pk=pk):
            interacao = Interacao.objects.get(pk=request.data['pk'])
            interacao.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={'token_error':'invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

