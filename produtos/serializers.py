from rest_framework import serializers
from produtos.models import Produto, Fornecedor, Categoria, Estoque

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            'id', 
            'nome_empresa', 
            'telefone',
            'cnpj'
        ]

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome'
        ]
class ProdutoSerializer(serializers.ModelSerializer):
    #fornecedor = FornecedorSerializer()
    #categoria = CategoriaSerializer()
    
    class Meta:
        model = Produto
        fields = ['id','nome','descricao','preco','disponivel','categoria','fornecedor']
        #fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = [
            'produto',
            'quantidade',
            'localizacao'
        ]