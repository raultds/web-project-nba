from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from NBAstats.forms import all_stars_form
from NBAstats.models import *

# Create your views here.
from api.APIrequests import team_request, player_request


def home(request):
    context = {}
    if not request.user.is_authenticated:
        context['allstars'] = False
    else:
        context['allstars'] = all_star.objects.filter(user_id=request.user).exists()

    return render(request, 'NBAstats/home.html', context)

class conference_detail(DetailView):
    model = conference
    template_name = 'NBAstats/conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['teams'] = team.objects.filter(conference_name=context['conference'].conference_name+"ern")
        context['title'] = context['conference'].conference_name + ' conference'
        if not self.request.user.is_authenticated:
            context['allstars'] = False
        else:
            context['allstars'] = all_star.objects.filter(user_id=self.request.user).exists()

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
        if not self.request.user.is_authenticated:
            context['allstars'] = False
        else:
            context['allstars'] = all_star.objects.filter(user_id=self.request.user).exists()
        return context


class player_detail(DetailView):
        model = player
        template_name = 'NBAstats/player_detail.html'
        context_object_name = 'player'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['stats'] = player_request(context['player'].name, context['player'].last_name, context['player'].player_id)
            if not self.request.user.is_authenticated:
                context['allstars'] = False
            else:
                context['allstars'] = all_star.objects.filter(user_id=self.request.user).exists()
            return context

class team_stats(DetailView):
    model = team
    template_name = 'NBAstats/team_stats.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['team'].team_name
        context['stats'] = team_request(context['team'].team_id)
        if not self.request.user.is_authenticated:
            context['allstars'] = False
        else:
            context['allstars'] = all_star.objects.filter(user_id=self.request.user).exists()
        return context


class my_done_all_stars(DetailView):
    model = all_star
    template_name = 'NBAstats/show_my_all_stars.html'
    context_object_name = 'all_stars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My All Stars"
        context['players'] = all_star.objects.filter(user_id=self.request.user)
        context['allstars'] = True
        print(context)
        return context


class all_all_stars(DetailView):
    pass


class my_all_stars(CreateView):
    model = all_star
    form_class = all_star
    template_name = 'NBAstats/myallstars.html'

    def get(self, request, *args, **kwargs):
        context = {'form': all_stars_form(request.POST)}
        return render(request, 'NBAstats/all_stars_form.html', context)

    def post(self, request, *args, **kwargs):
        form = all_stars_form(request.POST)
        if form.is_valid():
            all_star_instance = form.save()
            all_star_instance.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'NBAstats/all_stars_form.html', {'form': form})


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(my_all_stars, self).get_initial(**kwargs)
        initial['title'] = 'All Stars'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(my_all_stars, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class all_stars_update(UpdateView):
    model = all_star
    fields = "__all__"
    template_name = 'NBAstats/all_stars_update.html'

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        context = {'form': all_stars_form(request.POST)}
        return render(request, 'NBAstats/all_stars_update.html', context)

    def post(self, request, *args, **kwargs):
        form = all_stars_form(request.POST)
        if form.is_valid():
            all_star_instance = form.save()
            all_star_instance.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'NBAstats/all_stars_update.html', {'form': form})


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(my_all_stars, self).get_initial(**kwargs)
        initial['title'] = 'All Stars'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(my_all_stars, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs
