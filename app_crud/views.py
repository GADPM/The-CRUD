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

# Criar Novo Usuário
def criar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        Usuario.objects.create(nome=nome, email=email, telefone=telefone)
        return redirect('listar_usuarios')
    return render(request, 'app_crud/criar_usuario.html')

# Atualizar Usuário
def atualizar_usuario(request, id):
    # Usando 'id' para buscar o usuário
    usuario = get_object_or_404(Usuario, id=id)

    # Se a requisição for POST, atualiza os dados do usuário
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.save()
        return redirect('listar_usuarios')  # Redireciona para a lista de usuários

    # Se não for POST, renderiza o formulário de edição com os dados do usuário
    return render(request, 'app_crud/atualizar_usuario.html', {'usuario': usuario})

# Exemplo de função para deletar um usuário
def deletar_usuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return redirect('listar_usuarios')  # Redireciona de volta para a página de lista
    except Usuario.DoesNotExist:
        return redirect('listar_usuarios')  # Ou exibe uma mensagem de erro se o usuário não existir
