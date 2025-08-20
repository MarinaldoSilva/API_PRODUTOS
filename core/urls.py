from django.http import HttpResponse    
from django.contrib import admin
from django.urls import path, include
from produtos.urls import urlpatterns

def HomeView(request):
    return HttpResponse("Welcome to the API Produtos Home Page")

urlpatterns = [
    path("", HomeView), 
    path("admin/", admin.site.urls),
    path("api/v1/", include('core.api_urls')), 
]
