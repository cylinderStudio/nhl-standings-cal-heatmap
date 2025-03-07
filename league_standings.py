import requests
import plotly.colors as pc

BASE_URL = 'https://api-web.nhle.com/v1'

# Custom colorscales

blues = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(107,174,214)"],      # medium light blue
    [1.0, "rgb(8,48,107)"]          # dark blue
]

reds = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(252,187,161)"],      # medium light red
    [1.0, "rgb(203,24,29)"]         # full red
]

oranges = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(253,208,162)"],      # medium light orange
    [1.0, "rgb(217,72,1)"]          # full orange
]

greens = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(161,217,155)"],      # medium light green
    [1.0, "rgb(35,139,69)"]         # full green
]

greys = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(189,189,189)"],      # medium light grey
    [1.0, "rgb(82,82,82)"]          # full grey
]

yellows = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(255,237,160)"],      # medium light yellow
    [1.0, "rgb(255,204,0)"]         # deep, saturated yellow
]

golds = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(255,215,0)"],        # standard gold
    [1.0, "rgb(184,134,11)"]        # dark, rich gold (goldenrod)
]

teals = [
    [0.0, "rgb(255,255,255)"],      # white (for zero)
    [0.5, "rgb(128,255,255)"],      # light teal
    [1.0, "rgb(0,128,128)"]         # deep teal
]

team_color_scales = {
    'BOS': yellows,
    'BUF': blues,
    'DET': reds,
    'FLA': reds,
    'MTL': reds,
    'OTT': golds,
    'TBL': blues,
    'TOR': blues,
    'CAR': reds,
    'CBJ': blues,
    'NJD': reds,
    'NYI': oranges,
    'NYR': blues,
    'PHI': oranges,
    'PIT': golds,
    'WSH': reds,
    'UTA': teals,
    'CHI': reds,
    'COL': blues,
    'DAL': greens,
    'MIN': greens,
    'NSH': yellows,
    'STL': blues,
    'WPG': blues,
    'ANA': oranges,
    'CGY': reds,
    'EDM': blues,
    'LAK': greys,
    'SEA': teals,
    'SJS': teals,
    'VAN': blues,
    'VGK': golds,
}

def getStandings():
    standings = requests.get(BASE_URL+'/standings/now').json()['standings']

    standings_lists = {
        'A':[], "M":[], "C":[], "P": []
    }

    for x in standings:
        standings_lists[x['divisionAbbrev']].append(x)

    standings_lists['A'].sort(key=lambda e: e['divisionSequence'])
    standings_lists['M'].sort(key=lambda e: e['divisionSequence'])
    standings_lists['C'].sort(key=lambda e: e['divisionSequence'])
    standings_lists['P'].sort(key=lambda e: e['divisionSequence'])

    return standings_lists

def getColorScale(team):
    color_scale = team_color_scales[team]

    return color_scale
