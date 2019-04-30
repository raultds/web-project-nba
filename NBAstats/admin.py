from django.contrib import admin
from NBAstats import models
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(models.team)
admin.site.register(models.player)
admin.site.register(models.conference)
admin.site.register(models.all_star)
