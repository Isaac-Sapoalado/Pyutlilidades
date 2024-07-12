from rest_framework.serializers import ModelSerializer
from .models import Citacao

class CitacaoSerializer(ModelSerializer):

    class Meta:
        model = Citacao
        fields = ['citacao','autor']