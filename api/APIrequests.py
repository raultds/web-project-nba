import base64
import json

from pip._vendor import requests

# list_stats = ['OffReb', 'OffRebPerGame', 'DefReb', 'DefRebPerGame', 'Reb', 'RebPerGame', 'Ast', 'AstPerGame', 'Pts', 'PtsPerGame', 'Tov', 'TovPerGame', 'Stl', 'StlPerGame', 'Blk', 'BlkPerGame', 'BlkAgainst', 'BlkAgainstPerGame', 'PtsAgainst', 'PtsAgainstPerGame', 'Fouls', 'FoulsPerGame', 'FoulPers', 'FoulPersPerGame', 'FoulTech', 'FoulTechPerGame', 'PlusMinus', 'PlusMinusPerGame', 'FoulsDrawn', 'FoulsDrawnPerGame', 'FoulPersDrawn', 'FoulPersDrawnPerGame', 'FoulTechDrawn', 'FoulTechDrawnPerGame', 'FoulFlag1', 'FoulFlag1PerGame', 'FoulFlag1Drawn', 'FoulFlag1DrawnPerGame', 'FoulFlag2', 'FoulFlag2PerGame', 'FoulFlag2Drawn', 'FoulFlag2DrawnPerGame', 'Ejections']
def stats_request(list_stats, id):
    try:
        response = requests.get("https://api.mysportsfeeds.com/v1.2/pull/nba/2018-2019-regular/overall_team_standings.json",
            params={
                "team": str(id),         #FUNCIONA
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format("ba40fa50-4783-4820-b810-9dfa7b","nbastats1234").encode('utf-8')).decode('ascii')
            }
        )

        dic = json.loads(response.content)
        team_stats={}
        for stat in list_stats:
            team_stats[stat] = dic['overallteamstandings']['teamstandingsentry'][0]['stats'][stat]['#text']

        return(team_stats)

    except requests.exceptions.RequestException:
        return(0)

def team_results_request(id):
    list_stats = ['GamesPlayed', 'Wins', 'Losses', 'WinPct']
    return(stats_request(list_stats,id))

def team_2pts_request(id):
    list_stats = ['Fg2PtAtt', 'Fg2PtAttPerGame', 'Fg2PtMade', 'Fg2PtMadePerGame', 'Fg2PtPct']
    return(stats_request(list_stats,id))

def team_3pts_request(id):
    list_stats = ['Fg3PtAtt', 'Fg3PtAttPerGame', 'Fg3PtMade', 'Fg3PtMadePerGame', 'Fg3PtPct']
    return(stats_request(list_stats,id))

def team_fgs_request(id):
    list_stats = ['FgAtt', 'FgAttPerGame', 'FgMade', 'FgMadePerGame', 'FgPct']
    return(stats_request(list_stats,id))

def team_fts_request(id):
    list_stats = ['FtAtt', 'FtAttPerGame', 'FtMade', 'FtMadePerGame', 'FtPct']
    return(stats_request(list_stats,id))

def player_request(firstName, lastName, playerID):
    list_stats = ['GamesPlayed', 'Fg2PtAtt', 'Fg2PtAttPerGame', 'Fg2PtMade', 'Fg2PtMadePerGame', 'Fg2PtPct', 'Fg3PtAtt', 'Fg3PtAttPerGame', 'Fg3PtMade', 'Fg3PtMadePerGame', 'Fg3PtPct', 'FgAtt', 'FgAttPerGame', 'FgMade', 'FgMadePerGame', 'FgPct', 'FtAtt', 'FtAttPerGame', 'FtMade', 'FtMadePerGame', 'FtPct', 'OffReb', 'OffRebPerGame', 'DefReb', 'DefRebPerGame', 'Reb', 'RebPerGame', 'Ast', 'AstPerGame', 'Pts', 'PtsPerGame', 'Tov', 'TovPerGame', 'Stl', 'StlPerGame', 'Fouls', 'FoulsPerGame', 'FoulTech', 'FoulFlag1', 'FoulFlag2']
    try:
        response = requests.get("https://api.mysportsfeeds.com/v1.2/pull/nba/2018-2019-regular/cumulative_player_stats.json",
            params={
                "player": firstName + "-" + lastName + "-" + str(playerID)      #FUNCIONA
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format("ba40fa50-4783-4820-b810-9dfa7b","nbastats1234").encode('utf-8')).decode('ascii')
            }
        )

        dic = json.loads(response.content)
        player_stats={}
        for stat in list_stats:
            player_stats[stat] = dic['cumulativeplayerstats']['playerstatsentry'][0]['stats'][stat]['#text']

        return(player_stats)

    except requests.exceptions.RequestException:
        return(0)
