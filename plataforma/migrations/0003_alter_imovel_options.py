# Generated by Django 4.1.7 on 2023-03-21 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("plataforma", "0002_alter_imagem_options_alter_visitas_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imovel",
            options={"verbose_name": "Imóvel", "verbose_name_plural": "Imóveis"},
        ),
    ]
