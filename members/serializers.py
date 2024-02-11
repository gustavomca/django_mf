from .models import Pessoa, Membro
from datetime import date

from rest_framework import serializers
from utilidades.serializers import DynamicFieldsModelSerializer

class PessoaSerializer(DynamicFieldsModelSerializer):
    endereco_completo = serializers.SerializerMethodField()
    sexo_descricao = serializers.SerializerMethodField()
    idade = serializers.SerializerMethodField()
    data_nascimento = serializers.DateField(format='%d/%m/%Y')

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