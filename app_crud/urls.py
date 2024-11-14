from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('atualizar/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
