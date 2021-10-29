from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculos, Cliente, Venda
from .form import VeiculoForm, ClienteForm, VendaForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
@login_required
def home(request):
    veiculos = Veiculos.objects.all()

    return render(request, 'home.html', {'carro':veiculos})

@login_required
def novo_veiculo(request):
    form = VeiculoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(home)

    return render(request, 'form.html', {'form':form})

@login_required
def update_veiculo(request, id):
    veiculo = get_object_or_404(Veiculos, pk=id)
    form = VeiculoForm(request.POST or None, request.FILES or None, instance=veiculo)

    if form.is_valid():
        form.save()
        return redirect(home)

    return render(request, 'form.html', {'form':form})

@login_required
def delete_veiculo(request, id):
    veiculo = get_object_or_404(Veiculos, pk=id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect(home)

    return render(request, 'confirm.html')

@login_required
def novo_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(home)

    return render(request, 'formcliente.html', {'form':form})

@login_required
def vender(request):
    form = VendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_vendas)

    return render(request, 'venda.html', {'venda':form})


@login_required()
def lista_vendas(request):
    venda = Venda.objects.all()

    return render(request, 'lista-vendas.html', {'venda':venda})

def recibo(request, id):
    venda = get_object_or_404(Venda, pk=id)
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    dia = datetime.today().day
    mes_num = datetime.today().month
    mes = meses[mes_num]
    ano = datetime.today().year
    hora = datetime.today().strftime('%H:%M')

    return render(request, 'recibo.html', {'D':venda, 'dia':dia, 'mes':mes, 'ano':ano, 'hora':hora})