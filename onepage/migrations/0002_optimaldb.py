# Generated by Django 3.2.23 on 2024-01-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptimalDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Select_Model', models.CharField(choices=[('Select', 'Select'), ('lstm', 'LSTM'), ('gru', 'GRU'), ('saes', 'SAES'), ('new_saes', 'NEW_SAES'), ('rnn', 'RNN'), ('average', 'AVERAGE')], default='Select', max_length=20)),
                ('Source', models.IntegerField()),
                ('Destination', models.IntegerField()),
                ('Date_Time', models.DateTimeField(blank=True, null=True)),
                ('point', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]