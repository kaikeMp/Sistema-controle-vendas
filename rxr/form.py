from django.forms import ModelForm
from .models import Veiculos, Cliente, Venda

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculos
        fields = ['marca', 'modelo', 'placa', 'ano_fab', 'ano_mod', 'cor', 'renavam', 'chassi', 'foto', 'km','preco', 'preco_extenco']


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'rg', 'rua', 'num', 'bairro', 'cidade', 'estado', 'ddd', 'telefone']

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'veiculo', 'forma']