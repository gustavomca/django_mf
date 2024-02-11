from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'members'

router = routers.DefaultRouter()
router.register(r'pessoa',
                views.PessoaViewSet,
                basename='pessoa'),
router.register(r'membro',
                views.MembroViewSet,
                basename='membro'),

urlpatterns = [
    path('', include(router.urls)),
]