import pandas as pd
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title('NIFTY50 Stock Components')
st.markdown("""
NIFTY50 companies scraped from [Wikipedia](https://en.wikipedia.org/wiki/NIFTY_50)
""")

@st.cache
def download():
    url = 'https://en.wikipedia.org/wiki/NIFTY_50'
    html = pd.read_html(url, header = 0)
    df = html[1]
    return df

df = download()
sectors = df['Sector'].unique()


st.sidebar.header('Choose Sector')
selected = st.sidebar.multiselect('Sector', sorted(sectors))
values = ['Open', 'Close', 'Low', 'High']
selected2 = st.sidebar.selectbox('Value', values)

if len(selected)>0:
    st.header('Showing companies in ' + str(','.join(selected)) + ' sector')
selected_df = pd.DataFrame()
for sect in selected:
    selected_df = selected_df.append(df.loc[df['Sector']==sect], ignore_index = True)
if not selected_df.empty:
    st.dataframe(selected_df)
    tickers = list(selected_df.Symbol)
    for i in range(len(tickers)):
        tickers[i] = tickers[i] + '.NS'

    data = yf.download(tickers=tickers, period='ytd', interval='1d', group_by='ticker')

def plot(symbol):
    plot_df = pd.DataFrame(data[symbol][selected2])
    plot_df['Date'] = plot_df.index
    plt.fill_between(plot_df.Date, plot_df[selected2],alpha=0.2)
    plt.title(symbol, fontweight='bold')
    plt.plot(plot_df.Date, plot_df[selected2], alpha=1)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel(selected2)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    return st.pyplot()

if st.button('PLOT'):
    try:
        for ticker in tickers:
            plot(ticker)
    except Exception as e:
        st.write('Choose options from sidebar')
