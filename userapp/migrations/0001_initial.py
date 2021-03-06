# Generated by Django 4.0.3 on 2022-05-24 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurentapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookTableModel',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(max_length=100)),
                ('time', models.TimeField()),
                ('restaurent_name', models.CharField(max_length=100)),
                ('table_category', models.CharField(max_length=100)),
                ('members', models.CharField(max_length=100)),
                ('request', models.TextField()),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
            options={
                'db_table': 'user_booking_details',
            },
        ),
        migrations.CreateModel(
            name='UserRegModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_mobile', models.BigIntegerField()),
                ('user_password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_registration_details',
            },
        ),
        migrations.CreateModel(
            name='UserFeedbackModel',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='userapp.userregmodel')),
                ('user_booking', models.ForeignKey(db_column='user_booking', on_delete=django.db.models.deletion.CASCADE, to='userapp.userbooktablemodel')),
                ('user_restaurent', models.ForeignKey(db_column='user_restaurent', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurentapp.restaurentregmodel')),
                ('user_table', models.ForeignKey(db_column='user_table', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurentapp.restaurenttablemodel')),
            ],
            options={
                'db_table': 'user_feedback',
            },
        ),
        migrations.AddField(
            model_name='userbooktablemodel',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='userapp.userregmodel'),
        ),
        migrations.AddField(
            model_name='userbooktablemodel',
            name='user_restaurent',
            field=models.ForeignKey(db_column='user_restaurent', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurentapp.restaurentregmodel'),
        ),
        migrations.AddField(
            model_name='userbooktablemodel',
            name='user_table',
            field=models.ForeignKey(db_column='user_table', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurentapp.restaurenttablemodel'),
        ),
    ]
