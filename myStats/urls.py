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
from NBAstats.views import ConferenceDetail, TeamStats, TeamDetail, PlayerDetail, AllStarsUpdate, MyAllStars, \
	AllAllStars, UserAllStars, AllStarsDelete
from NBAstats.models import Team, Player, Conference
from django.views.generic.detail import DetailView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.Home, name="home"),
	path('conference/<int:pk>', ConferenceDetail.as_view(), name='conference_detail'),
	path('conference/team/stats/<int:pk>', TeamStats.as_view(), name='team_stats'),
	path('conference/team/<int:pk>', TeamDetail.as_view(), name='team_detail'),
	path('conference/team/player/<int:pk>', PlayerDetail.as_view(), name='player_detail'),
	path('accounts/login/', djangoViews.LoginView.as_view(), name='login'),
	path('accounts/logout/', djangoViews.LogoutView.as_view(), name='logout'),
	path('myallstars/', MyAllStars.as_view(), name='my_all_stars'),
	path('myallstars/update', AllStarsUpdate.as_view(), name='my_all_stars_update'),
	path('myallstars/delete', AllStarsDelete.as_view(), name='my_all_stars_delete'),
	path('allstars/', views.AllAllStars, name='all_all_stars'),
	path('allstars/user/<int:pk>', UserAllStars.as_view(), name='user_all_stars'),
]
