# Generated by Django 3.0.3 on 2020-02-11 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_is_superuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Team',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='groups',
            new_name='teams',
        ),
    ]
