import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Horoscope using streamlit app')
st.markdown(""" ##### From [Horoscope.com](https://www.horoscope.com/us/index.aspx) """)
st.markdown("""---""")

zodiac_sign = {  "Pick one": 0,
    "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12 }

#list of days
day = [ "Pick one",
        "today",
        "yesterday",
        "tomorrow",
        "weekly",
        "monthly",
        "yearly"]

def find_horoscope(a,b):
    if day.index(b) < 4:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{b}.aspx?sign={zodiac_sign[a]}")
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.findAll('div', {'class': 'main-horoscope'})
    elif day.index(b) > 3 and day.index(b) < 6:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-{b}.aspx?sign={zodiac_sign[a]}")
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.findAll('div', {'class': 'main-horoscope'})
    else:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/yearly/2022-horoscope-{a.lower()}.aspx")
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.findAll('section', {'class': 'tab-content'})

    for item in data:
        res = item.p.text
    st.write(res)

with st.sidebar:
    a = st.selectbox('Pick your Zodiac Sign', zodiac_sign)
    st.markdown("""---""")
    b = st.selectbox('Pick time value', day)

find_horoscope(a,b)
