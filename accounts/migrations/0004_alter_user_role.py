# Generated by Django 4.0.6 on 2022-08-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer')], null=True),
        ),
    ]
