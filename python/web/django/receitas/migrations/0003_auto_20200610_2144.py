# Generated by Django 2.2 on 2020-06-11 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='pessoa',
        ),
        migrations.AlterField(
            model_name='receita',
            name='nome_receita',
            field=models.CharField(max_length=100),
        ),
    ]
