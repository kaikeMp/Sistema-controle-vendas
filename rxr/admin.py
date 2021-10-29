from django.contrib import admin
from .models import Veiculos, Cliente, Venda

class VeiculosAdmin(admin.ModelAdmin):
    fields = ['marca', 'modelo', 'placa', 'ano_fab', 'ano_mod', 'cor', 'renavam', 'chassi', 'foto', 'km','preco', 'preco_extenco']
    list_display = ['id', 'marca', 'modelo', 'placa', 'ano_fab', 'ano_mod', 'cor', 'km','preco']
    list_filter = ['marca', 'modelo', 'placa', 'ano_fab', 'ano_mod', 'cor', 'km','preco']
    search_fields = ['marca', 'modelo', 'placa', 'ano_fab', 'ano_mod', 'cor', 'km','preco']

class ClienteAdmin(admin.ModelAdmin):
    fields = ['nome', 'sobrenome', 'cpf', 'rg', 'rua', 'num', 'bairro', 'cidade', 'estado', 'ddd', 'telefone']
    list_display = ['nome', 'sobrenome']
    list_filter =  ['nome', 'sobrenome', 'bairro', 'cidade', 'estado', 'ddd']
    search_fields = ['nome', 'sobrenome', 'bairro', 'cidade', 'estado', 'ddd']

class VendaAdmin(admin.ModelAdmin):
    fields = ['cliente', 'veiculo', 'forma']
    list_display = ['cliente', 'veiculo']
    list_filter = ['cliente']
    search_fields = ['cliente']


admin.site.register(Veiculos, VeiculosAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)