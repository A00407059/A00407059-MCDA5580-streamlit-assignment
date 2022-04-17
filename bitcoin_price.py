# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:27:03 2022

@author: Jongwon Shinn
"""

import pandas as pd
import requests
import streamlit as st


#initialize the values
days = '0'
vs_currency = 'CAD'

st.title('Bitcoin price trends by Jongwon Shinn(A00407059)')

#get # days and currency using slider and radio button
var_1 = st.slider(days, max_value=100)

var_2 = st.radio(
     "Select the currency",
     ('cad', 'usd', 'inr'))

# set the url and get request
payload = {'vs_currency': var_2, 'days': var_1, 'interval': 'daily' }
r = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart', params=(payload))


if r.status_code==200:
    data = r.json()
    

#get the data and transformed to dataframe.
raw_data=data['prices']
df = pd.DataFrame(raw_data, columns= ['date', 'prices'])

df['date'] = pd.to_datetime(df['date'], unit='ms')

df.plot.line(x='date', y='prices')


#plot line chart
st.line_chart(df.rename(columns={'date':'index'}).set_index('index'))

