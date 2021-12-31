import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.write("""
### Simple streamlit app

This shows the **GOOGLE** stock pricing 101

""")
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
### DF info
""")
tickerDf

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
