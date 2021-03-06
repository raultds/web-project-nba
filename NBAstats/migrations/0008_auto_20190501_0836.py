# Generated by Django 2.1.7 on 2019-05-01 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBAstats', '0007_team_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_star',
            name='player_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_1', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_10', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_11', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_12', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_2', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_3', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_4', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_5', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_6', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_7', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_8', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='all_star',
            name='player_9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_9', to='NBAstats.Player'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='NBAstats'),
        ),
    ]
