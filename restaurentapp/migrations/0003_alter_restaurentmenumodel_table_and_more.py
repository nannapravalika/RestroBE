# Generated by Django 4.0.1 on 2022-04-20 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurentapp', '0002_restaurentregmodel_status'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='restaurentmenumodel',
            table='restaurent_menu_details',
        ),
        migrations.AlterModelTable(
            name='restaurentregmodel',
            table='restaurent_registration_details',
        ),
    ]
