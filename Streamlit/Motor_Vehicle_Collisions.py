# Guided Project on Coursera: https://www.coursera.org/projects/data-science-streamlit-python

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px


st.set_page_config(layout='wide')

st.markdown("## A dashboard to analyze Motor_Vehicle_Collisions in NYC")

st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv('Motor_Vehicle_Collisions.csv', nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace="True")
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)
og_data = data

injured_people = st.slider('Choose number of people injured', 0, 19)
st.map(data.query('injured_persons >= @injured_people')[['latitude', 'longitude']].dropna(how='any'))

st.header('Collisions by hour')
hour = st.slider('Choose Hour', 0, 23)
data = data[data['date/time'].dt.hour == hour]

st.write(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state = {
    "latitude": np.average(data['latitude']),
    "longitude": np.average(data['longitude']),
    "zoom": 11,
    "pitch": 50,
    },
    layers=[
        pdk.Layer(
        'HexagonLayer',
        data=data[['date/time', 'latitude', 'longitude']],
        get_position=['longitude', 'latitude'],
        radius=100,
        extruded=True,
        pickable=True,
        elevation_scale=4,
        elevation_range=[0,1000],
        ),
    ],
))

st.subheader('Collsion Breakdown by minute and hour')
filtered = data[
        (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour+1))
]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'crashes': hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig)

st.header('Top 5 dangerous streets to different poeple')
select = st.selectbox('Type', ['pedestrians', 'cyclists', 'motorists'])
if select == 'pedestrians':
    st.write(og_data.query('injured_pedestrians >= 1')[['on_street_name', 'injured_pedestrians']].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how='any')[:5])

elif select == 'cyclists':
    st.write(og_data.query('injured_cyclists >= 1')[['on_street_name', 'injured_cyclists']].sort_values(by=['injured_cyclists'], ascending=False).dropna(how='any')[:5])

else:
    st.write(og_data.query('injured_motorists >= 1')[['on_street_name', 'injured_motorists']].sort_values(by=['injured_motorists'], ascending=False).dropna(how='any')[:5])

if st.button('Show Raw Data'):
    st.subheader('RAW DATA')
    st.write(data)
