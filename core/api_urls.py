from django.urls import path, include

urlpatterns = [
    path('', include("produtos.urls")),
    path('auth/', include('accounts.urls'))
]