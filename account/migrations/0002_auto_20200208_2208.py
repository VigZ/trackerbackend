# Generated by Django 3.0.3 on 2020-02-08 22:08

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]
