# Generated by Django 3.0.3 on 2020-02-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200211_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='environment',
            field=models.CharField(blank=True, max_length=30, verbose_name='environment'),
        ),
    ]
