# Generated by Django 2.2.5 on 2020-06-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAILWAYAPP', '0010_auto_20200614_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengerdata',
            name='seatnumber',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='passengerdata',
            name='seatstatus',
            field=models.CharField(default='', max_length=30),
        ),
    ]