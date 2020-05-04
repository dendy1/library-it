# Generated by Django 3.0.6 on 2020-05-04 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_auto_20200504_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carditem',
            name='given_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 17, 57, 59, 600561)),
        ),
        migrations.AlterField(
            model_name='carditem',
            name='returned_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 17, 57, 59, 600561)),
        ),
        migrations.AlterField(
            model_name='carditem',
            name='status',
            field=models.CharField(default='На руках', max_length=64),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
