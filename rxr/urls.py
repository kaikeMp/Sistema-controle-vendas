from .views import home, novo_veiculo, update_veiculo, delete_veiculo, novo_cliente, vender, lista_vendas, recibo
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('novo/', novo_veiculo, name='adicionar_veiculo'),
    path('update/<int:id>/', update_veiculo, name='update_veiculo'),
    path('delete/<int:id>/', delete_veiculo, name='delete_veiculo'),
    path('novocliente/', novo_cliente, name='novo_cliente'),
    path('venda/', vender, name='novavenda'),
    path('lista_vendas/', lista_vendas, name='lista_de_vendas'),
    path('recibo/<int:id>/', recibo, name='recibo')
]