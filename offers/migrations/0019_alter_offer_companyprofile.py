# Generated by Django 3.2.6 on 2021-12-06 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0031_rename_companytypes_companytype'),
        ('offers', '0018_offer_companyprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='companyProfile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='profiles.recruiterprofile'),
        ),
    ]
