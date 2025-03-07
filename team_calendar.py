import pandas as pd
import numpy as np
from plotly_calplot import calplot
import requests

SEASON_START_DATE = '2024-10-04'
SEASON_END_DATE = '2025-04-17'
BASE_URL = 'https://api-web.nhle.com/v1'

def getSchedule(team):
    results = requests.get(BASE_URL+'/club-schedule-season/'+team+'/20242025').json()['games']
    return results

def generatePlot(team,colorscale):

    game_schedule = getSchedule(team)

    team_score = 0
    opponent_score = 0

    date_range = pd.date_range(start=SEASON_START_DATE, end=SEASON_END_DATE).strftime('%Y-%m-%d')
    # Fill entire frame with zero for empty or "no game" dates
    data_frame = pd.DataFrame(0, index=pd.Index(date_range,name='dates'), columns=['outcomes'])

    for i in range(len(game_schedule)):
        # regular season game type = 2
        if game_schedule[i]['gameType'] == 2 and 'score' in game_schedule[i]['awayTeam']:        
            if game_schedule[i]['awayTeam']['abbrev'] == team:
                team_score = game_schedule[i]['awayTeam']['score']
                opponent_score = game_schedule[i]['homeTeam']['score']
            else:
                team_score = game_schedule[i]['homeTeam']['score']
                opponent_score = game_schedule[i]['awayTeam']['score']
            
            x = team_score - opponent_score

            if x > 0: outcome = 3       # win
            elif x < 0: outcome = 1     # loss
            else: outcome = 0

            # change dates where a game occured to have a non-zero outcome
            game_date = game_schedule[i]['gameDate']
            data_frame.loc[game_date, 'outcomes'] = outcome

    '''To use the named index of dates for the x-axis, 
    Ploty requires converting the index to a column'''
    data_frame_reset = data_frame.reset_index()

    fig = calplot(
        data_frame_reset, 
        x='dates',
        y='outcomes', 
        dark_theme=True, 
        colorscale=colorscale,
        years_title=True,
        start_month=1,
        end_month=12,
        years_as_columns=True,
        month_lines_width=3,
        month_lines_color='#000000',
        show_empty_months=False,
        gap=2,
    )

    fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))

    # fig.update_traces(hovertemplate='%{customdata[0]}: %{z}<extra></extra>')
    fig.update_layout(hovermode=False)

    # fig.show()
    return fig