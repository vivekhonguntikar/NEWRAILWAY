# Generated by Django 2.2.5 on 2020-03-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAILWAYAPP', '0004_auto_20200309_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('concession', models.CharField(max_length=30)),
            ],
        ),
    ]
