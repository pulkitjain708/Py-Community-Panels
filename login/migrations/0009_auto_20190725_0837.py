# Generated by Django 2.2.3 on 2019-07-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190724_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
