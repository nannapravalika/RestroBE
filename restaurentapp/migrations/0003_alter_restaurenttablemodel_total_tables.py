# Generated by Django 4.0.3 on 2022-05-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurentapp', '0002_restaurenttablemodel_total_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurenttablemodel',
            name='total_tables',
            field=models.CharField(max_length=100),
        ),
    ]
