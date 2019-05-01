"""myStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as djangoViews
from NBAstats import views
from NBAstats.views import conference_detail, team_stats, team_detail, player_detail, all_stars_update, my_all_stars, \
	my_done_all_stars, all_all_stars, user_all_stars
from NBAstats.models import team, player, conference
from django.views.generic.detail import DetailView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
	path('conference/<int:pk>', conference_detail.as_view(), name='conference_detail'),
	path('conference/team/stats/<int:pk>', team_stats.as_view(), name='team_stats'),
	path('conference/team/<int:pk>', team_detail.as_view(), name='team_detail'),
	path('conference/team/player/<int:pk>', player_detail.as_view(), name='player_detail'),
	path('accounts/login/', djangoViews.LoginView.as_view(), name='login'),
	path('accounts/logout/', djangoViews.LogoutView.as_view(), name='logout'),
	path('myallstars/', my_all_stars.as_view(), name='my_all_stars'),
	path('myallstars/update', all_stars_update.as_view(), name='my_all_stars_update'),
	path('myallstars/show', views.my_done_all_stars, name='show_my_all_stars'),
	path('allstars/', views.all_all_stars, name='all_all_stars'),
    path('allstars/user/<int:pk>', user_all_stars.as_view(), name='user_all_stars'),


]
