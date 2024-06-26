# Generated by Django 3.2.23 on 2024-01-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0010_delete_flowdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptimalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Select_Model', models.CharField(choices=[('Select', 'Select'), ('lstm', 'LSTM'), ('gru', 'GRU'), ('saes', 'SAES'), ('new_saes', 'NEW_SAES'), ('rnn', 'RNN'), ('average', 'AVERAGE')], default='Select', max_length=20)),
                ('Source', models.IntegerField(default=2911)),
                ('Destination', models.IntegerField(default=4013)),
                ('Date_Time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
