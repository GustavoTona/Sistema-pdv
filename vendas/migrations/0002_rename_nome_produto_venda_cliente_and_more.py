# Generated by Django 5.0.1 on 2024-02-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='nome_produto',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='venda',
            old_name='preco',
            new_name='produto',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='primeiro_nome',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='sobrenome',
        ),
    ]
