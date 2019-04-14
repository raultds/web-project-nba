#!/usr/bin/env python

"""
    Script to import player data from .csv file to Model Database DJango
    To execute this script run:
                                1) manage.py shell
                                2) exec(open('script_player_csv.py').read())
"""

import csv
from NBAstats.models import player

CSV_PATH = 'players.csv'

contSuccess = 0
# Remove all data from Table
player.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',')
    print('Loading...')
    for row in spamreader:
        print(row)
        player.objects.create(player_id=row[0], name=row[1], last_name=row[2], jersey_num=row[3], position=row[4], height = row[5], weight=row[6], birth_date=row[7], birth_city=row[8], birth_country=row[9], team_id=row[10], team_abbr=row[11], team_city=row[12], team_name=row[13], player_photo=row[14])
        contSuccess += 1
    print('{str(contSuccess)} inserted successfully! ')
