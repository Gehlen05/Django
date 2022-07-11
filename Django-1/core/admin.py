from django.contrib import admin

from .models import Produto, Cliente


class ProdutoAdimn(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome',  'email')


admin.site.register(Produto, ProdutoAdimn)
admin.site.register(Cliente, ClienteAdmin)
