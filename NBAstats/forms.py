from django import forms

from NBAstats.models import AllStars


class all_stars_form(forms.ModelForm):
	class Meta:
		model = AllStars
		exclude = ('user_id',)


class all_stars_update_form(forms.ModelForm):
	class Meta:
		model = AllStars
		exclude = ('user_id',)
