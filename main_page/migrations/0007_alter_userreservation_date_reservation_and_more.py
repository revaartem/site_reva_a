# Generated by Django 4.1.5 on 2023-02-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_userreservation_date_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='date_reservation',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='time_reservation',
            field=models.CharField(max_length=10),
        ),
    ]
