# Generated by Django 3.2.6 on 2021-08-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0009_auto_20210813_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
