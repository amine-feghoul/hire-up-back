# Generated by Django 3.2.6 on 2021-12-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=150, unique=True)),
            ],
        ),
    ]
