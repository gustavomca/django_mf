from django.db import models

# Create your models here.
class Pessoa(models.Model):
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField()
    endereco_logradouro = models.CharField(max_length=200, null=True, blank=True)
    endereco_numero = models.CharField(max_length=20, null=True, blank=True)
    endereco_complemento = models.CharField(max_length=200, null=True, blank=True)
    endereco_bairro = models.CharField(max_length=100, null=True, blank=True)
    endereco_cep = models.CharField(max_length=10, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=15, null=True, blank=True)
    telefone_celular = models.CharField(max_length=15, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=gender_choices)
    ativo = models.BooleanField(default=True)
    visitante = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

class Membro(models.Model):

    igreja = models.ForeignKey('church.Igreja', on_delete=models.CASCADE)
    membro = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='membro')
    ativo = models.BooleanField(default=True)
    ausente = models.BooleanField(default=False)
    baixa_frequencia = models.BooleanField(default=False)
    necessidades_especiais = models.BooleanField(default=False)
    profissao_fe = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.membro.nome} ({self.numero})'


class RegistroAtaMembro(models.Model):
    tipo_registro_choices = [
        ('A', 'Admissão'),
        ('D', 'Desligamento'),
        ('P', 'Profissão de Fé'),
    ]

    tipo_admissao_choices = [
        ('B', 'Batismo'),
        ('T', 'Transferência'),
        ('J', 'Jurisdição'),   
    ]

    tipo_desligamento_choices = [
        ('E', 'Exclusão'),
        ('T', 'Transferência'),
        ('F', 'Falecimento'),
    ]

    igreja = models.ForeignKey('church.Igreja', on_delete=models.CASCADE, related_name='registros_atas')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='registros_ata')
    tipo_registro = models.CharField(max_length=1, choices=tipo_registro_choices)
    tipo_admissao = models.CharField(max_length=1, choices=tipo_admissao_choices, null=True, blank=True)
    tipo_desligamento = models.CharField(max_length=1, choices=tipo_desligamento_choices, null=True, blank=True)
    data = models.DateField()
    livro = models.CharField(max_length=10)
    ata = models.CharField(max_length=10)
    folha = models.CharField(max_length=10, null=True, blank=True)
    numero = models.CharField(max_length=10)
    ano = models.CharField(max_length=10)
    observacao = models.TextField()

    def __str__(self):
        return f'{self.membro.membro.nome} ({self.data})'
    

class Oficial(models.Model):
    cargo_choices = [
        ('Pr', 'Pastor'),
        ('Pb', 'Presbítero'),
        ('Dc', 'Diácono'),
    ]

    membro = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=2, choices=cargo_choices)
    inicio_mandato = models.DateField()
    fim_mandato = models.DateField(blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Oficiais'

    def __str__(self):
        return f'{self.membro.nome} ({self.get_cargo_display()})'
    
    def save(self, *args, **kwargs):
        self.fim_mandato = self.inicio_mandato.replace(year=self.inicio_mandato.year + 5)
        super(Oficial, self).save(*args, **kwargs)