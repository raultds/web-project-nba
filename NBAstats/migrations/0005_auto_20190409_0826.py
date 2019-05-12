# Generated by Django 2.1.5 on 2019-04-09 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBAstats', '0004_conference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='NBAstats.Conference'),
        ),
    ]
