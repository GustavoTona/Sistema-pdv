# Generated by Django 5.0.1 on 2024-02-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_quantidade_alter_produto_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.IntegerField(max_length=50, verbose_name='Preço'),
        ),
    ]
