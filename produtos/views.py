from .models import Produto, Fornecedor, Categoria, Estoque
from .serializers import ProdutoSerializer, FornecedorSerializer, CategoriaSerializer, EstoqueSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class ProdutoViewset(viewsets.ModelViewSet):
    queryset = Produto.objects.all() 
    """retorna a lista de todos os produtos"""
    serializer_class = ProdutoSerializer 
    """os produtos serem serializados com o ProdutoSerializer e transformados em JSON, os fields que são retornados são os que são permitios no ProdutoSerializer"""


    """verifica se o usuário está autenticado se não estiver, não pode criar, editar ou apagar mas pode ver os produtos por isso, usamos IsAuthenticatedOrReadOnly"""
    authentication_classes = [TokenAuthentication]

    """aqui é feita a verificação do pedido, se for get, deixa passar, se for post, put ou delete, verifica se o usuário está autenticado se não estiver autenticado, não pode criar, editar ou apagar, mas pode ver os produtos"""
    permission_classes = [IsAuthenticatedOrReadOnly]

class FornecedorViewset(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CategoriaViewsets(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticatedOrReadOnly]

class EstoqueViewset(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticatedOrReadOnly]