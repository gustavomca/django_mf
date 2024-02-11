from .models import Pessoa, Membro
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import PessoaSerializer

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