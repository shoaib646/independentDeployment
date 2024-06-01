# Generated by Django 3.2.23 on 2024-01-28 00:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=265)),
                ('email_or_contact', models.CharField(max_length=265, validators=[django.core.validators.RegexValidator(message='Please enter a valid email or contact number.', regex='^(\\d{10}|\\w+@\\w+\\.\\w{2,3})$')])),
                ('subject', models.CharField(blank=True, max_length=265)),
                ('message', models.CharField(blank=True, max_length=265)),
            ],
        ),
    ]