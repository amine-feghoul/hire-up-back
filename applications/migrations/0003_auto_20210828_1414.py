# Generated by Django 3.2.6 on 2021-08-28 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20210814_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicationState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='on_hold', max_length=150, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='condidateId',
            new_name='condidate_id',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='employerId',
            new_name='employer_id',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='offerId',
            new_name='offer_id',
        ),
        migrations.AddField(
            model_name='applications',
            name='state',
            field=models.ForeignKey(default='on_hold', on_delete=django.db.models.deletion.SET_DEFAULT, to='applications.applicationstate', to_field='state'),
        ),
    ]
