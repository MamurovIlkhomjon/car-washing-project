# Generated by Django 4.1.1 on 2022-10-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='car',
            name='car_model, car_owner and car_phone error',
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='role and washcompany error',
        ),
        migrations.RemoveConstraint(
            model_name='washer',
            name='name and phone error',
        ),
    ]
