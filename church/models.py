from django.db import models

# Create your models here.
class Igreja(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco_logradouro = models.CharField(max_length=200, null=True, blank=True)
    endereco_numero = models.CharField(max_length=20, null=True, blank=True)
    endereco_complemento = models.CharField(max_length=200, null=True, blank=True)
    endereco_bairro = models.CharField(max_length=100, null=True, blank=True)
    endereco_cep = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome