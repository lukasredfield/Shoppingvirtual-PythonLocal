# Generated by Django 4.1 on 2022-10-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_rename_contenido_productos_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
