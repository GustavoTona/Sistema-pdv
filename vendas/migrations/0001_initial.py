# Generated by Django 5.0.1 on 2024-01-31 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('nome_produto', models.CharField(max_length=50)),
                ('preco', models.CharField(max_length=50)),
            ],
        ),
    ]
