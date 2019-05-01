from django import forms

from NBAstats.models import all_star


class all_stars_form(forms.ModelForm):
	class Meta:
		model = all_star
		fields = ('player_1', 'player_2', 'player_3', 'player_4', 'player_5', 'player_6', 'player_7', 'player_8', 'player_9', 'player_10', 'player_11', 'player_12')
