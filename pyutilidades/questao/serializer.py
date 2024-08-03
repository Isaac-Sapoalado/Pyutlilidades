from rest_framework import serializers
from .models import Questao,Alternativa

class Questao_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Questao
        fields = ['pk','questao','banca','assunto','concurso']

class Alternativa_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Alternativa
        fields = ['alternativa','certo','questao']