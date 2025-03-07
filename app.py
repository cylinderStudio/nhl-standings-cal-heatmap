import team_calendar
import league_standings
import streamlit as st
import datetime
import uuid

st.set_page_config(page_title='NHL Current Standings and Team Win/Loss Heatmaps', layout='wide')
st.logo(
    './assets/sports_hockey.svg',
    size='large',
    icon_image='./assets/sports_hockey.svg'
)

standings = league_standings.getStandings()

st.markdown(f'''
    #### NHL Current Standings and Team Win/Loss Heatmaps
    **2024 - 2025 Season** | {datetime.date.today().strftime('%B %#d, %Y')}
''')

atlantic_tab, metropolitan_tab, central_tab, pacific_tab = st.tabs(['Atlantic Division', 
    'Metropolitan Division', 'Central Division', 'Pacific Division'])


def renderStandings(divLetter):

    for i in standings[divLetter]:
        st.write((str(i['divisionSequence']) + '. ' + str(i['teamName']['default']) + '\n'))

        colorscale = league_standings.getColorScale(str(i['teamAbbrev']['default']))

        calender = team_calendar.generatePlot(str(i['teamAbbrev']['default']),colorscale)
        st.plotly_chart(calender, theme='streamlit', use_container_width=True, key=uuid.uuid4())

        legend_items = {
            "Win": colorscale[2][1],
            "Loss": colorscale[1][1],
        }

        legend_html = """
        <div style=div style="display: flex; align-items: center; flex-wrap: wrap;">
        """
        for label, color in legend_items.items():
            legend_html += f"""
        <div style="display: inline-flex; align-items: center; margin-right: 10px;">
            <div style="width: 15px; height: 15px; background-color: {color}; margin-right: 3px;"></div>
            <span style="font-size: 12px;">{label}</span>
        </div>
        """

        legend_html += "</div>"

        # Display the legend in Streamlit
        st.markdown(legend_html, unsafe_allow_html=True)

        st.divider()

st.markdown(''' <a target="_self" href="#nhl-current-standings-and-team-win-loss-heatmaps">
                    <button>
                        Back to Top
                    </button>
                </a>''', unsafe_allow_html=True)

with atlantic_tab:
    with st.container():
        st.markdown('##### Atlantic Division')
        renderStandings('A')
    
with metropolitan_tab:
    with st.container():
        st.markdown('##### Metropolitan Division')
        renderStandings('M')

with central_tab:
    with st.container():
        st.markdown('##### Central Division')
        renderStandings('C')
    
with pacific_tab:
    with st.container():
        st.markdown('##### Pacific Division')
        renderStandings('P')