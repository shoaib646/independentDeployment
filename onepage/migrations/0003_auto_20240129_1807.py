# Generated by Django 3.2.23 on 2024-01-29 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0002_optimaldb'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictFlowDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='optimaldb',
            name='point',
        ),
    ]
