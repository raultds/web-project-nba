from functools import reduce

from behave import *
import operator
from django.db.models import Q
import os

from myStats.settings import BASE_DIR

use_step_matcher("parser")

@given('Exists all_star by "{username}"')
def step_impl(context, username):
	from django.contrib.auth.models import  User
	user = User.objects.get(username=username)
	from NBAstats.models import all_star
	all_stars = all_star.objects.get(user_id=username)
	all_stars.save()

@when('I register all_star at user "{username}')
def step_impl(context, username):
	from django.contrib.auth.models import User
	user = User.objects.get(username=username)
	for row in context.table:
		context.browser.visit(context.get_url('myStats:user_all_stars'), user.pk)
		#TODO