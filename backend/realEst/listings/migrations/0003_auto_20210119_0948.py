# Generated by Django 3.1.2 on 2021-01-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210118_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
