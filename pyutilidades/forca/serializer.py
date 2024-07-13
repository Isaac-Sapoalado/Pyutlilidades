from rest_framework.serializers import ModelSerializer,StringRelatedField
from .models import Palavra,Dica

class Palavraserializer(ModelSerializer):
    dicas = StringRelatedField(many=True)

    class Meta:
        model = Palavra
        fields = ['palavra','dicas']
        

class Dicaserializer(ModelSerializer):
    class Meta:
        model = Dica
        fields = ['dica']