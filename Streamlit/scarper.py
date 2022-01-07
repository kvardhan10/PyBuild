import streamlit as st
import requests
from bs4 import BeautifulSoup
import numpy as np
from matplotlib import pyplot as plt
import  wikipedia
import pyttsx3
import yfinance as yf
import pandas as pd

st.title('Web Scraping Toolsets')

def covidDetails():
    st.header('Covid Details')
    page=requests.get("https://www.worldometers.info/coronavirus/")

    soup= BeautifulSoup(page.text,'lxml')

    table=soup.find('table',id="main_table_countries_today")

    headers=[ heading.text.replace(",Other","") for heading in table.find_all('th')]

    table_rows=[ row for row in table.find_all('tr')]

    results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]
    name = st.selectbox('Choose country', [ 'World','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'UK', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
    for i in results:
        if "Country" in i:
            if i["Country"]==name:
                st.write(i)
                qty = [float(i['TotalCases'].replace(',', '')), float(i['TotalDeaths'].replace(',', '')), float(i['TotalRecovered'].replace(',', '')), float(i['ActiveCases'].replace(',', '')), float(i['Serious,Critical'].replace(',', ''))]
                of = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical']
                explode = (0.2, 0.2, 0.2, 0.2, 0.2)
                fig1, ax1 = plt.subplots()
                ax1.pie(qty, explode=explode, labels=of, autopct='%1.1f%%', radius=2)
                st.pyplot(fig1)

def wikiSumm():
    st.header('Wikipedia Summarizer')
    value = st.text_input('Search what you want??')
    values = wikipedia.summary(value)
    # engine = pyttsx3.init()
    st.write(values)
    # engine.say(values)
    # engine.runAndWait()
    # engine.stop()

def weather():
    st.header('Weather Details')
    city = st.text_input("Enter city name to get weather details\n");
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all data
    st.write(city," weather details are as follows\n");
    st.write("Temperature is", temp)
    st.write("Time is ", time)
    st.write("Sky Description: ", sky)
    st.write(other_data)

    # # initialisation
    # engine = pyttsx3.init()
    #
    # # testing
    # engine.say(city)
    # engine.say("weathers details are as follows")
    # engine.say("Temperature is")
    # engine.say(temp)
    # engine.say("Time is ")
    # engine.say( time)
    # engine.say("Sky Description: ")
    # engine.say( sky)
    # engine.say(other_data)
    # engine.runAndWait()
    #

def stocks():
    st.header('STOCK PRICING 101')
    tickerSymbol = st.selectbox('Pick one', ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOGL', 'FB', 'NVDA', 'JPM', 'BAC', 'ADBE', 'NFLX', 'PFE', 'DIS' ,'WMT'])
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

    st.write("""
    ### Closing price
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ### Volume price
    """)
    st.line_chart(tickerDf.Volume)

    st.write("""
    ### Open price
    """)
    st.line_chart(tickerDf.Open)

    st.write("""
    ### Low price
    """)
    st.line_chart(tickerDf.Low)

    st.write("""
    ### High price
    """)
    st.line_chart(tickerDf.High)

    st.write("""
    ### Dividends
    """)
    st.line_chart(tickerDf.Dividends)

    st.write("""
    ### Recommendations
    """)
    tickerData.recommendations

    st.write("""
    ### Calendar
    """)
    tickerData.calendar

    st.write("""
    ### Company Data
    """)
    tickerData.info

def horoscope():
    st.subheader('Horoscope')
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

    a = st.selectbox('Pick your Zodiac Sign', zodiac_sign)
    b = st.selectbox('Pick time value', day)
    find_horoscope(a,b)

with st.sidebar:
    a = st.selectbox('Select one:', ['Choose One','Covid Details', 'Wikipedia Summarizer', 'Weather Details', 'Horoscope', 'Stocks'])
    st.markdown("""---""")

if a == 'Covid Details':
    covidDetails()

if a == 'Wikipedia Summarizer':
    wikiSumm()

if a == 'Weather Details':
    weather()

if a == 'Stocks':
    stocks()

if a == 'Horoscope':
    horoscope()
