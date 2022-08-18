from django.contrib import admin
from .models import Pessoa, Contato


@admin.action(description='Ativar selecionados')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)


@admin.action(description='Desativar selecionados')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'ativa',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo'
    ]

    actions = [
        ativar_todos,
        desativar_todos
    ]


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)
