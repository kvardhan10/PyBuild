import streamlit as st
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from urllib.request import urlopen, Request
import time as tm
import  wikipedia
import yfinance as yf
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.downloader.download('vader_lexicon')

st.title('Web Scraping Toolsets')

def covidDetails():
    st.header('Covid Details')
    page=requests.get("https://www.worldometers.info/coronavirus/")

    soup= BeautifulSoup(page.text,'lxml')

    table=soup.find('table',id="main_table_countries_today")

    headers=[ heading.text.replace(",Other","") for heading in table.find_all('th')]

    table_rows=[ row for row in table.find_all('tr')]

    results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]
    name = st.selectbox('Choose country', [ 'World','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'UK', 'USA', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])
    with st.spinner(text='In progress'):
        tm.sleep(3)
        for i in results:
            if "Country" in i:
                if i["Country"]==name:
                    st.write(i)
                    qty = [float(i['TotalCases'].replace(',', '')), float(i['TotalDeaths'].replace(',', '')), float(i['TotalRecovered'].replace(',', '')), float(i['ActiveCases'].replace(',', '')), float(i['Serious,Critical'].replace(',', ''))]
                    of = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical']
                    explode = (0.1, 0.1, 0.1, 0.1, 0.1)
                    fig1, ax1 = plt.subplots()
                    ax1.pie(qty, explode=explode, labels=of, autopct='%1.1f%%', radius=2)
                    st.pyplot(fig1)

def wikiSumm():
    st.header('Wikipedia Summarizer')
    value = st.text_input('Search what you want??')
    values = wikipedia.summary(value)
    # engine = pyttsx3.init()
    with st.spinner(text='In progress'):
        tm.sleep(3)
        st.write(values)

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
    with st.spinner(text='In progress'):
        tm.sleep(3)

        st.write(city," weather details are as follows\n");
        st.metric("Temperature is", temp)
        st.metric("Time is ", time)
        st.metric("Sky Description: ", sky)

def stocks():
    st.header('STOCK PRICING')
    tickerSymbol = st.selectbox('Pick one', ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'GOOGL', 'FB', 'NVDA', 'JPM', 'BAC', 'ADBE', 'NFLX', 'PFE', 'DIS' ,'WMT'])


    start = st.date_input('Enter start date')
    end = st.date_input('Enter end date')

    with st.spinner(text='In progress'):
        tm.sleep(3)

        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period='1d', start=start, end=end)
        current_price = tickerData.info['currentPrice']
        day_low = tickerData.info['dayLow']
        day_high = tickerData.info['dayHigh']
        st.metric(label="Current value (in USD)", value=current_price)
        st.metric(label="Day High", value=day_high, delta=(current_price-day_high))
        st.metric(label="Day Low", value=day_low, delta=(current_price-day_low))

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

    #     st.write("""
    # ### Recommendations
    # """)
    #     tickerData.recommendations

    #     st.write("""
    # ### Company Data
    # """)
    #     tickerData.info

        qty = [tickerData.info['totalCash'], tickerData.info['totalDebt'], tickerData.info['totalRevenue']]
        of = ['Total Cash', 'Total Debt', 'Total Revenue']
        explode = (0.1, 0.1, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(qty, explode=explode, labels=of, autopct='%1.1f%%', radius=2)
        st.pyplot(fig1)

        st.subheader('What\'s new?')
        finviz_url = 'https://finviz.com/quote.ashx?t='
        url = finviz_url + tickerSymbol

        req = Request(url=url, headers={'user-agent': 'my-app'})
        response = urlopen(req)

        html = BeautifulSoup(response, features='html.parser')
        news_table = html.find(id='news-table')
        parsed_data = []

        for row in news_table.findAll('tr'):
            title = row.a.text
            atag = row.a
            date_data = row.td.text.split(' ')
            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]
            link = atag['href']
            st.write(tickerSymbol + " " + date + " " + time + " " + title)
            st.write(link)
            parsed_data.append([tickerSymbol,date,time,title])
            df=pd.DataFrame(parsed_data,columns=['tickerSymbol','date','time','title'])
            vader=SentimentIntensityAnalyzer()
            f=lambda title: vader.polarity_scores(title)['compound']
            df['compound']=df['title'].apply(f)
            st.write(df.head())
            df['date']=pd.to_datetime(df.date).dt.date
            plt.figure(figsize=(6,4))
            mean_df=df.groupby(['tickerSymbol','date']).mean()
            mean_df=mean_df.unstack()
            mean_df=mean_df.xs('compound',axis="columns").transpose()
            # fig, ax = plt.subplots()
            # ax = mean_df.plot(kind='bar')
            # st.pyplot(fig)
            st.markdown("""---""")

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
        with st.spinner(text='In progress'):
            tm.sleep(3)
            st.write(res)

    a = st.selectbox('Pick your Zodiac Sign', zodiac_sign)
    b = st.selectbox('Pick time value', day)
    find_horoscope(a,b)

with st.sidebar:
    st.header('Choose one of the toolset')
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
