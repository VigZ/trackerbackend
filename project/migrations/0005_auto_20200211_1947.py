# Generated by Django 3.0.3 on 2020-02-11 19:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_auto_20200211_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='completed_date',
            field=models.DateTimeField(blank=True, help_text='The date the ticket was completed', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='due_date',
            field=models.DateTimeField(blank=True, help_text='The date before which the ticket is to be completed', null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='steps_to_reproduce',
            field=models.CharField(blank=True, max_length=1000, verbose_name='steps_to_reproduce'),
        ),
        migrations.CreateModel(
            name='TicketGrouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('resolution_order', models.CharField(max_length=1000, verbose_name='resolution_order')),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project.Project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('comment_text', models.CharField(max_length=1000, verbose_name='comment_text')),
                ('poster', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Poster')),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project.Ticket', verbose_name='Ticket')),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_grouping',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='project.TicketGrouping', verbose_name='Ticket Grouping'),
        ),
    ]