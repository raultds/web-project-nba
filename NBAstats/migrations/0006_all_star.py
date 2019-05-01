# Generated by Django 2.0 on 2019-04-30 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NBAstats', '0005_auto_20190409_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_1', to='NBAstats.player')),
                ('player_10', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_10', to='NBAstats.player')),
                ('player_11', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_11', to='NBAstats.player')),
                ('player_12', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_12', to='NBAstats.player')),
                ('player_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_2', to='NBAstats.player')),
                ('player_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_3', to='NBAstats.player')),
                ('player_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_4', to='NBAstats.player')),
                ('player_5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_5', to='NBAstats.player')),
                ('player_6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_6', to='NBAstats.player')),
                ('player_7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_7', to='NBAstats.player')),
                ('player_8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_8', to='NBAstats.player')),
                ('player_9', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_9', to='NBAstats.player')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]