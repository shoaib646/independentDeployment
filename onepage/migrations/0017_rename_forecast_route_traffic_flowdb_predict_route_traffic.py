# Generated by Django 4.1.5 on 2024-02-10 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0016_rename_predict_route_traffic_flowdb_forecast_route_traffic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flowdb',
            old_name='Forecast_Route_Traffic',
            new_name='Predict_Route_Traffic',
        ),
    ]