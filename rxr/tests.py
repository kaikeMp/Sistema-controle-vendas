from django.test import TestCase
from .models import *

class VeiculoTestCase(TestCase):
    def setUp(self):
        Veiculos.objects.create(marca = 'Hyundai', modelo='Azera', placa='AZE1R46', ano_fab='2020', ano_mod='2021', cor='Preto', renavam='789456423', chassi='456asf4s5d63', foto='teste.jpg', km='1000',preco='70000', preco_extenco='setenta mil reais')