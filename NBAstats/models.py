from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.validators import ASCIIUsernameValidator
from datetime import date, datetime
from django import *
from django.views.generic import ListView, DetailView

# Create your models here.


class Conference(models.Model):
    conference_id = models.IntegerField(blank=False, primary_key=True)
    conference_name = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.conference_name


class Team(models.Model):
    team_id = models.IntegerField(blank=False, primary_key=True)
    conference_name = models.CharField(blank=True, null=True, max_length=20)
    team_abbr = models.CharField(blank=True, null=True, max_length=3)
    team_city = models.CharField(blank=True, null=True, max_length=20)
    team_name = models.CharField(blank=True, null=True, max_length=15)
    conference = models.ForeignKey(Conference, default=1, on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to="NBAstats", blank=True, null=True)
    def __str__(self):
        return self.team_city + ' ' + self.team_name

    def get_absolute_url(self):
        return reverse('myStats:team_detail', kwargs={'pk': self.team_id})


class Player(models.Model):
    player_id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=True, null=True, max_length=30)
    jersey_num = models.IntegerField(blank=True)
    position = models.CharField(blank=True, null=True, max_length=2)
    height = models.CharField(blank=True, null=True, max_length=10)
    weight = models.IntegerField(blank=True)
    birth_date = models.CharField(blank=True, null=True, max_length=15)
    birth_city = models.CharField(blank=True, null=True, max_length=30)
    birth_country = models.CharField(blank=True, null=True, max_length=15)
    team_id = models.IntegerField(default=0, null=True)
    team_abbr = models.CharField(blank=True, null=True, max_length=3)
    team_city = models.CharField(blank=True, null=True, max_length=20)
    team_name = models.CharField(blank=True, null=True, max_length=15)
    player_photo = models.ImageField(upload_to="NBAstats", blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('myStats:player_detail', kwargs={'pk': self.player_id})


class AllStars(models.Model):
    user_id = models.ForeignKey(User, blank=False, unique=True, on_delete=models.CASCADE)
    player_1 = models.ForeignKey(Player, related_name='player_1', null=True, blank=True, on_delete=models.SET_NULL)
    player_2 = models.ForeignKey(Player, related_name='player_2', null=True, blank=True, on_delete=models.SET_NULL)
    player_3 = models.ForeignKey(Player, related_name='player_3', null=True, blank=True, on_delete=models.SET_NULL)
    player_4 = models.ForeignKey(Player, related_name='player_4', null=True, blank=True, on_delete=models.SET_NULL)
    player_5 = models.ForeignKey(Player, related_name='player_5', null=True, blank=True, on_delete=models.SET_NULL)
    player_6 = models.ForeignKey(Player, related_name='player_6', null=True, blank=True, on_delete=models.SET_NULL)
    player_7 = models.ForeignKey(Player, related_name='player_7', null=True, blank=True, on_delete=models.SET_NULL)
    player_8 = models.ForeignKey(Player, related_name='player_8', null=True, blank=True, on_delete=models.SET_NULL)
    player_9 = models.ForeignKey(Player, related_name='player_9', null=True, blank=True, on_delete=models.SET_NULL)
    player_10 = models.ForeignKey(Player, related_name='player_10', null=True, blank=True, on_delete=models.SET_NULL)
    player_11 = models.ForeignKey(Player, related_name='player_11', null=True, blank=True, on_delete=models.SET_NULL)
    player_12 = models.ForeignKey(Player, related_name='player_12', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user_id.pk) + ' ' + self.user_id.username

    def get_absolute_url(self):
        return self.user_id.pk
