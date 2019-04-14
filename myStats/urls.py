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
from NBAstats.views import team_detail, conference_detail, player_detail, team_stats
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
]
