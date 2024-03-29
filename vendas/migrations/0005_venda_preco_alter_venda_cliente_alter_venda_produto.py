# Generated by Django 5.0.1 on 2024-02-01 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0002_produto_quantidade_alter_produto_created_at_and_more'),
        ('vendas', '0004_auto_20240201_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
        ),
    ]
