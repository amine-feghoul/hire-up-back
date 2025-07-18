# Generated by Django 3.2.6 on 2021-08-28 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0011_alter_offer_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='contractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(default='', max_length=150, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offerCategory',
            new_name='offer_category',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offerTitle',
            new_name='offer_title',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offerType',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='skills',
        ),
        migrations.AlterField(
            model_name='offer',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='offerSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.offer')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.skills', to_field='skill')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='contract_type',
            field=models.ForeignKey(default='CDD', on_delete=django.db.models.deletion.SET_DEFAULT, to='offers.contracttype', to_field='contract_type'),
        ),
    ]
