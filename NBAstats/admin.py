from django.contrib import admin
from NBAstats import models
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(models.Team)
admin.site.register(models.Player)
admin.site.register(models.Conference)
admin.site.register(models.AllStars)
