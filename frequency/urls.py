from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'frequency'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]