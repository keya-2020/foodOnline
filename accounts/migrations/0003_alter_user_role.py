# Generated by Django 4.0.6 on 2022-08-05 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'vendor'), (2, 'Customer')], null=True),
        ),
    ]
