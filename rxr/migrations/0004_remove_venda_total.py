# Generated by Django 3.2.8 on 2021-10-16 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rxr', '0003_venda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='total',
        ),
    ]
