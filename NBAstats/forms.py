from django import forms

from NBAstats.models import all_star


class all_stars_form(forms.ModelForm):
	class Meta:
		model = all_star
		exclude = ('user_id',)

class all_stars_update_form(forms.ModelForm):
	class Meta:
		model = all_star
		exclude = ('user_id',)
