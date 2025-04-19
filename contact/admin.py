from django.contrib import admin
from contact import models

@admin.register(models.Cadastros)
class CadastrosAdmin(admin.ModelAdmin):
    list_display = 'id', 'numero_apt', 'nome_morado', 'tipo_entrega',
    ordering = '-id',
    list_display_links = 'numero_apt', 'nome_morado',