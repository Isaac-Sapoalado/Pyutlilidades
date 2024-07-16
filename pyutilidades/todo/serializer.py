from rest_framework.serializers import ModelSerializer
from .models import Tarefa

class Tarefa_serializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['tarefa', 'feito','user']
    