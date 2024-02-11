from django.contrib import admin

from .models import Membro, Oficial, Pessoa

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Membro)
admin.site.register(Oficial)
