from django.contrib.auth import get_user_model
from rest_framework import serializers
from app_corretora.models import Cliente, Produtos, ProdutosDoCliente

class ClienteSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class ProdutoDoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutosDoCliente
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'password'

        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
 