# Generated by Django 3.2.6 on 2021-09-02 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_rename_postion_profilemodel_position_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='position_id',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='position',
            field=models.ForeignKey(default='poistion', on_delete=django.db.models.deletion.CASCADE, to='profiles.positions', to_field='position'),
        ),
    ]
