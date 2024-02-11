from .models import Pessoa, Membro, Oficial
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import PessoaSerializer, MembroSerializer, OficialSerializer

# Create your views here.
class PessoaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PessoaSerializer(queryset,
                many=True,
                fields=('id', 'nome', 'data_nascimento',
                        'endereco_completo', 'endereco_cep',
                        'sexo_descricao', 'idade', 'situacao'))
        return Response(serializer.data)
    
    
class MembroViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Membro.objects.all().order_by('membro__nome')
    serializer_class = MembroSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MembroSerializer(queryset,
                many=True,
                fields=('id', 'nome', 'data_nascimento', 'info_ata', 'ano','situacao'))
        return Response(serializer.data)


class OficialViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Oficial.objects.all().order_by('membro__nome')
    serializer_class = OficialSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OficialSerializer(queryset,
                many=True,
                fields=('id', 'nome', 'cargo_descricao', 'inicio_mandato', 'fim_mandato','mandato_vigente'))
        return Response(serializer.data)