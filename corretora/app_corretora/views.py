from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed
from app_corretora.serialaizers import ClienteSerialiazer, ProdutoSerialiazer, ProdutoDoClienteSerializer, UserSerializer
from app_corretora.models import Cliente, Produtos, ProdutosDoCliente
from django.contrib.auth import get_user_model


class ClienteViewsSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerialiazer
    permission_classes = [IsAuthenticated]

    
class ProdutoViewsSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerialiazer
    permission_classes = [IsAuthenticated]


class ProdutoDoClienteViewsSet(viewsets.ModelViewSet):
    queryset = ProdutosDoCliente.objects.all()
    serializer_class = ProdutoDoClienteSerializer
    permission_classes = [IsAuthenticated]

    def listar_produtos_por_cliente(self, request):
        if request.method != 'GET':
            # Gera um erro MethodNotAllowed para métodos diferentes de GET
            raise MethodNotAllowed(request.method)  

        prod_clientes = {}
        for produto in self.get_queryset():
            cpf_cliente = produto.cpf_cliente
            if cpf_cliente and cpf_cliente not in prod_clientes:
                prod_clientes[cpf_cliente] = []
            if cpf_cliente:  # Verifica se o CPF do cliente não está vazio
                prod_clientes[cpf_cliente].append({
                    'cpf_cliente': cpf_cliente,
                    'nome_cliente': produto.nome_cliente,
                    'nome_produto': produto.nome_produto,
                    'tipo': produto.tipo,
                    'liquidez': produto.liquidez
                })
    
        return Response(prod_clientes)
       
class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects
    serializer_class = UserSerializer
    http_method_names = ['post']

