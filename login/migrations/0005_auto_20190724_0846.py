# Generated by Django 2.2.3 on 2019-07-24 08:46

import constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190724_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[(constants.Gender('Male'), 'Male'), (constants.Gender('Female'), 'Female')], max_length=5),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='status',
            field=models.CharField(choices=[(constants.Status('Pending'), 'Pending'), (constants.Status('Confirmed'), 'Confirmed')], max_length=5),
        ),
    ]
