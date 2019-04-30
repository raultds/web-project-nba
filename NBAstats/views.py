from django.shortcuts import render
from django.views.generic import ListView, DetailView
from NBAstats.models import *

# Create your views here.
from api.APIrequests import team_request, player_request


def home(request):
    return render(request, 'NBAstats/home.html', None)

class conference_detail(DetailView):
    model = conference
    template_name = 'NBAstats/conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['teams'] = team.objects.filter(conference_name=context['conference'].conference_name+"ern")
        context['title'] = context['conference'].conference_name + ' conference'

        return context

class team_detail(DetailView):
    model = team
    template_name = 'NBAstats/team_detail.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['players'] = player.objects.filter(team_name=context['team'].team_name)
        context['title'] = context['team'].team_name
        context['stats'] = team_request(context['team'].team_id)
        return context

class player_detail(DetailView):
        model = player
        template_name = 'NBAstats/player_detail.html'
        context_object_name = 'player'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['stats'] = player_request(context['player'].name, context['player'].last_name, context['player'].player_id)
            return context

class team_stats(DetailView):
    model = team
    template_name = 'NBAstats/team_stats.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['team'].team_name
        context['stats'] = team_request(context['team'].team_id)
        return context

def myallstars(request):
    return render(request, 'NBAstats/myallstars.html', None)
