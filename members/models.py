from django.db import models

# Create your models here.
class Membro(models.Model):
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco_logradouro = models.CharField(max_length=200, null=True, blank=True)
    endereco_numero = models.CharField(max_length=20, null=True, blank=True)
    endereco_complemento = models.CharField(max_length=200, null=True, blank=True)
    endereco_bairro = models.CharField(max_length=100, null=True, blank=True)
    endereco_cep = models.CharField(max_length=10, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=15, null=True, blank=True)
    telefone_celular = models.CharField(max_length=15, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

class MembroRol(models.Model):
    membro = models.OneToOneField(Membro, on_delete=models.CASCADE)
    livro = models.CharField(max_length=10)
    ata = models.CharField(max_length=10)
    folha = models.CharField(max_length=10, null=True, blank=True)
    numero = models.CharField(max_length=10)
    ano = models.CharField(max_length=10)
    data_recepcao = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    ausente = models.BooleanField(default=False)
    baixa_frequencia = models.BooleanField(default=False)
    necessidades_especiais = models.BooleanField(default=False)
    profissao_fe = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.membro.nome} ({self.numero})'