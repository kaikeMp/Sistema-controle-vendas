# Generated by Django 3.2.8 on 2021-10-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rxr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('cpf', models.IntegerField(blank=True, null=True)),
                ('rg', models.IntegerField(blank=True, null=True)),
                ('rua', models.CharField(max_length=200)),
                ('num', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('ddd', models.IntegerField(blank=True, null=True)),
                ('telefone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='veiculos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Preço'),
        ),
    ]