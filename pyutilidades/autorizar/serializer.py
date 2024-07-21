from rest_framework import serializers
from django.contrib.auth.models import User




class UsuarioSerializer(serializers.ModelSerializer):
    # significa que "password" será só recebido(request)
    # mas não devolvido(response)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['pk','username', 'password', 'email']

    def create(self, validate_data):
        # Esse método é chamdo no save() do serializer
        # ele camada o .create() do Model
        # validate_data são o dados já verificados (se estao ok)
        # user = User.objects.create_user(
        #     username=validate_data['username'], password=validate_data['password'], )
        user = User.objects.create_user(**validate_data)
        return user