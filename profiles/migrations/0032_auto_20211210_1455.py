# Generated by Django 3.2.6 on 2021-12-10 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_rename_companytypes_companytype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='nationality',
        ),
    ]
