# Generated by Django 3.1.4 on 2021-01-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_estado_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginacecyte',
            name='carpeta',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
