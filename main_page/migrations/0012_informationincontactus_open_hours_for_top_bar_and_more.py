# Generated by Django 4.1.5 on 2023-02-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationincontactus',
            name='open_hours_for_top_bar',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informationincontactus',
            name='phone_for_top_bar',
            field=models.CharField(default='test', max_length=15),
            preserve_default=False,
        ),
    ]
