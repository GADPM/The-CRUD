from django.db import models

class Usuario(models.Model):
    # Django cria um campo ID por padrão, então não precisamos declarar
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone com até 15 caracteres

    def __str__(self):
        return f"{self.nome} - {self.email}"

    # Você pode criar um método customizado para representar o ID, se necessário
    @property
    def custom_id(self):
        return f"USR-{self.id}"  # Exemplo: USR-1, USR-2, ...
