from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

# Criar um novo usuário
def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'app_crud/criar_usuario.html', {'form': form})

# Listar todos os usuários
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_crud/listar_usuarios.html', {'usuarios': usuarios})

# Atualizar usuário
def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'app_crud/atualizar_usuario.html', {'form': form, 'usuario': usuario})

# Excluir usuário
def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usuarios')
