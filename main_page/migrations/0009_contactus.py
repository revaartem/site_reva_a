# Generated by Django 4.1.5 on 2023-02-07 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_thisisfortest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=63, validators=[django.core.validators.RegexValidator(message='Standard e-mail form', regex='^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\\.)+[a-z0-9]{1}([a-z0-9-]*[a-z0-9])?$')])),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date_of_the_request', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_of_the_request',),
            },
        ),
    ]
