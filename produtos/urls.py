from rest_framework.routers import DefaultRouter
from .views import ProdutoViewset, FornecedorViewset, CategoriaViewsets, EstoqueViewset


router = DefaultRouter()
#registro das rotas
router.register(r'produtos', ProdutoViewset)
router.register(f'fornecedores', FornecedorViewset)
router.register(f'categorias', CategoriaViewsets)
router.register(f'estoque', EstoqueViewset)

#adiciona as rotas ao urlpatterns
urlpatterns = router.urls