# Generated by Django 3.2.6 on 2021-08-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20210828_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='profilePic',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='recruiterprofile',
            old_name='companyLogo',
            new_name='company_logo',
        ),
        migrations.RenameField(
            model_name='recruiterprofile',
            old_name='profilePic',
            new_name='profile_pic',
        ),
    ]
