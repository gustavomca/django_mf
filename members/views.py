from .models import Pessoa, Membro, Oficial
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .filters import OficialFilter

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
    
    def create(self, request, *args, **kwargs):
        serializer = MembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class OficialViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Oficial.objects.all().order_by('membro__nome')
    serializer_class = OficialSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = OficialFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = OficialSerializer(queryset,
                many=True,
                fields=('id', 'nome', 'cargo_descricao', 'inicio_mandato', 'fim_mandato','mandato_vigente'))
        return Response(serializer.data)