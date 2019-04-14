#!/usr/bin/env python

"""
    Script to import team data from .csv file to Model Database DJango
    To execute this script run:
                                1) manage.py shell
                                2) exec(open('script_team_csv.py').read())
"""

import csv
from NBAstats.models import team

CSV_PATH = 'teams.csv'

contSuccess = 0
# Remove all data from Table
team.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    print('Loading...')
    for row in spamreader:
        team.objects.create(team_id=row[0], conference_name=row[1], team_abbr=row[2], team_city=row[3], team_name=row[4])
        contSuccess += 1
    print('{str(contSuccess)} inserted successfully! ')
