# Generated by Django 3.2.8 on 2021-10-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=99)),
                ('placa', models.CharField(max_length=7)),
                ('ano_fab', models.IntegerField(blank=True, null=True, verbose_name='Ano de Fabricação')),
                ('ano_mod', models.IntegerField(blank=True, null=True, verbose_name='Ano Modelo')),
                ('cor', models.CharField(max_length=50)),
                ('renavam', models.IntegerField()),
                ('chassi', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('km', models.IntegerField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Preço')),
            ],
        ),
    ]