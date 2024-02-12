from .models import Pessoa, Membro, Oficial
from django_filters import rest_framework as filters


class OficialFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='membro__nome', lookup_expr='icontains')
    cargo = filters.CharFilter(field_name='cargo', lookup_expr='iexact')
    ano_vencimento = filters.NumberFilter(method='filter_ano_vencimento')

    class Meta:
        model = Oficial
        fields = []

    def filter_ano_vencimento(self, queryset, name, value):
        return queryset.filter(fim_mandato__year=value)
