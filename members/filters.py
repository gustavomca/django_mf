from .models import Pessoa, Membro, Oficial
from django_filters import rest_framework as filters
from datetime import date
from django.db.models import Q


class OficialFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='membro__nome', lookup_expr='icontains')
    cargo = filters.CharFilter(field_name='cargo', lookup_expr='iexact')
    mandato_vigente = filters.BooleanFilter(method='filter_mandato_vigente')
    ano_vencimento = filters.NumberFilter(method='filter_ano_vencimento')

    class Meta:
        model = Oficial
        fields = []

    def filter_ano_vencimento(self, queryset, name, value):
        return queryset.filter(fim_mandato__year=value)
    
    def filter_mandato_vigente(self, queryset, name, value):
        today = date.today()
        if value:
            return queryset.filter(Q(fim_mandato__gte=today) & Q(inicio_mandato__lte=today))
        else:
            return queryset.filter(Q(fim_mandato__lt=today) | Q(inicio_mandato__gt=today))
