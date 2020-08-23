# Generated by Django 2.2.5 on 2020-03-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RAILWAYAPP', '0002_addtraindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainroute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainno', models.CharField(max_length=6)),
                ('trainfrom', models.CharField(max_length=50)),
                ('trainto', models.CharField(max_length=30)),
                ('route', models.CharField(max_length=30)),
                ('departuretime', models.CharField(max_length=30)),
                ('arrivaltime', models.CharField(max_length=30)),
            ],
        ),
    ]
