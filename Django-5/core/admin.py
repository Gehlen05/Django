from django.contrib import admin
from .models import Chassi, Carro, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, objeto):
        return ','.join([motorista.username for motorista in objeto.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'
