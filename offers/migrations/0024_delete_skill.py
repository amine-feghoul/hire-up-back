# Generated by Django 3.2.6 on 2021-12-24 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0039_auto_20211224_2010'),
        ('offers', '0023_auto_20211224_2010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
