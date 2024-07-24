from rest_framework import serializers
from .models import Tarefa

class Tarefa_serializer(serializers.ModelSerializer):

    class Meta:
        model = Tarefa
        fields = ['tarefa', 'feito','pk','user']
    