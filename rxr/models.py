from django.db import models

class Veiculos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=99)
    placa = models.CharField(max_length=7)
    ano_fab = models.IntegerField('Ano de Fabricação', null=True, blank=True)
    ano_mod = models.IntegerField('Ano Modelo', null=True, blank=True)
    cor = models.CharField(max_length=50)
    renavam = models.IntegerField()
    chassi = models.CharField(max_length=50)
    foto = models.ImageField(null=True, blank=True)
    km = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField('Preço',max_digits=8, decimal_places=2, null=True)
    preco_extenco = models.CharField('Preço Por Extenso', max_length=200, null=True, blank=True)

    def get_completemodel(self):
        return self.marca + ' ' + self.modelo

    def __str__(self):
        return self.get_completemodel()

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.IntegerField(null=True, blank=True)
    rg = models.IntegerField(null=True, blank=True)
    rua = models.CharField(max_length=200)
    num = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    ddd = models.IntegerField(null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)

    def get_completename(self):
        return self.nome + ' ' + self.sobrenome

    def complete_endereco(self):
        return self.rua + ', ' + self.num + ', ' + self.bairro + ', ' + self.cidade + '-' + self.estado

    def __str__(self):
        return self.get_completename()

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    veiculo = models.OneToOneField(Veiculos, on_delete=models.CASCADE, null=True)
    forma = models.CharField(max_length=500, null=True, blank=True)