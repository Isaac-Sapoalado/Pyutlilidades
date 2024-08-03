from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from autorizar.views import verificar_token,verificar_user
from .models import Questao,Alternativa,Banca,Assunto,Materia
from .serializer import Questao_Serializer,Alternativa_Serializer
from rest_framework.permissions import AllowAny


class Questao_View(APIView):

    permission_classes = [AllowAny]

    def get(self,request):
        questoes = Questao.objects.all()
        serializer =  Questao_Serializer(questoes,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request):
        questao = Questao_Serializer(data=request.data)
        questao.is_valid(raise_exception=True)
        questao.save()
        return Response(questao.data,status.HTTP_201_CREATED)

class Questao_Detail_View(APIView):

    permission_classes = [AllowAny]

    def get_object(self,query,text):

        objeto = Questao.objects.all()
            
        if query == 'banca':
            pk = Banca.objects.get(banca=text).pk
            objeto = Questao.objects.filter(banca=pk)
            
        if query == 'assunto':
            pk = Assunto.objects.get(assunto=text).pk
            objeto = Questao.objects.filter(assunto=pk)
            
        if query == 'materia':
            pk = Materia.objects.get(materia=text).pk
            objeto = Questao.objects.filter(materia=pk)

        return objeto

    def get(self,request,filtro):
        try:
            queue,banca = filtro.split(",")
            serializer  = Questao_Serializer(instance=self.get_object(queue,banca),many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(data={'error':'erroau'},status=200)

