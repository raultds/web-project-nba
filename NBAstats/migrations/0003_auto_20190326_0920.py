# Generated by Django 2.0.13 on 2019-03-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBAstats', '0002_auto_20190326_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
