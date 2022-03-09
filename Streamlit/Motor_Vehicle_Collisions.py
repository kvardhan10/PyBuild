import streamlit as st
import pandas as pd
import numpy as np

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

if st.button('Show Raw Data'):
    st.subheader('RAW DATA')
    st.write(data)
