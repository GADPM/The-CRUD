# app_crud/urls.py

from django.urls import path
from . import views  # Isso importa as views do arquivo views.py

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('atualizar_usuario/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('deletar_usuario/<int:id>/', views.deletar_usuario, name='deletar_usuario'),  # Aqui você associa a URL com a view
]