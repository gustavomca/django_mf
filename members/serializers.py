from .models import Pessoa, Membro, Oficial
from datetime import date

from rest_framework import serializers
from utilidades.serializers import DynamicFieldsModelSerializer


class PessoaSerializer(DynamicFieldsModelSerializer):
    endereco_completo = serializers.SerializerMethodField()
    sexo_descricao = serializers.SerializerMethodField()
    idade = serializers.SerializerMethodField()
    data_nascimento = serializers.DateField(format='%d/%m/%Y')
    situacao = serializers.SerializerMethodField()

    class Meta:
        model = Pessoa
        fields = '__all__'
        depth = 1

    def get_endereco_completo(self, obj):
        endereco_completo = f'{obj.endereco_logradouro}, {obj.endereco_numero}'
        if obj.endereco_complemento:
            endereco_completo += f', {obj.endereco_complemento}'
        endereco_completo += f' - {obj.endereco_bairro}'
        return endereco_completo
    
    def get_sexo_descricao(self, obj):
        return obj.get_sexo_display()
    
    def get_idade(self, obj):
        today = date.today()
        return today.year - obj.data_nascimento.year - ((today.month, today.day) < (obj.data_nascimento.month, obj.data_nascimento.day))

    def get_situacao(self, obj):
        if hasattr(obj, 'membro'):
            if obj.membro.profissao_fe:
                return 'Membro Maior'
            else:
                return 'Membro Menor'
        else:
            return 'Visitante'
        
        
class MembroSerializer(DynamicFieldsModelSerializer):
    nome = serializers.SerializerMethodField()
    data_nascimento = serializers.SerializerMethodField()
    info_ata = serializers.SerializerMethodField()
    data_recepcao = serializers.DateField(format='%d/%m/%Y')
    situacao = serializers.SerializerMethodField()

    class Meta:
        model = Membro
        fields = [
            'id',
            'nome',
            'data_nascimento',
            'livro',
            'ata',
            'folha',
            'numero',
            'ano',
            'data_recepcao',
            'situacao',
            'info_ata',
            'ausente',
            'baixa_frequencia',
            'necessidades_especiais',
            'profissao_fe',
            'membro'
        ]

    def get_nome(self, obj):
        return obj.membro.nome
    
    def get_data_nascimento(self, obj):
        return obj.membro.data_nascimento.strftime('%d/%m/%Y')

    def get_situacao(self, obj):
        if obj.profissao_fe:
            return 'Membro Maior'
        else:
            return 'Membro Menor'
    
    def get_info_ata(self, obj):
        infoata = f'livro {obj.livro}, ata {obj.ata}'
        if obj.folha:
            infoata += f', folha {obj.folha}'
        return infoata


class OficialSerializer(DynamicFieldsModelSerializer):
    nome = serializers.SerializerMethodField()
    cargo_descricao = serializers.SerializerMethodField()
    inicio_mandato = serializers.DateField(format='%d/%m/%Y')
    fim_mandato = serializers.DateField(required=False, format='%d/%m/%Y')
    mandato_vigente = serializers.SerializerMethodField()

    class Meta:
        model = Oficial
        fields = [
            'id',
            'nome',
            'cargo',
            'cargo_descricao',
            'inicio_mandato',
            'fim_mandato',
            'mandato_vigente',
            'membro'
        ]

    def get_nome(self, obj):
        return obj.membro.nome

    def get_cargo_descricao(self, obj):
        return obj.get_cargo_display()

    def get_mandato_vigente(self, obj):
        today = date.today()
        return obj.inicio_mandato <= today and obj.fim_mandato >= today