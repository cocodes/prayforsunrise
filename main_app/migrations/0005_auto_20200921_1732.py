# Generated by Django 3.1 on 2020-09-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200921_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='eaten',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='executed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]