from django import forms

from NBAstats.models import all_star


class all_stars_form(forms.ModelForm):
	class Meta:
		model = all_star
		fields = "__all__"
