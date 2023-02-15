#!/usr/bin/python3

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from datetime import datetime
import time

t = 0
st.set_page_config("Analytical Dashboard", layout="wide",page_icon='🤑')

# forex_daily
fx_url = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=INR&apikey=X01AA6ACSC2VWDLJ&datatype=csv"
# crypto_daily
crypt_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=X01AA6ACSC2VWDLJ&datatype=csv"

st.title("ML Smart App Live Dashboard")

# use cryptocur and countries as filters for your dashboard

st.markdown(
    """
<style>
header{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
</style>
""",
    unsafe_allow_html=True,
)


def get_fx_csv(key1="USD", key2="INR"):
    return pd.read_csv(
        "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol="
        + key1
        + "&to_symbol="
        + key2
        + "&apikey=X01AA6ACSC2VWDLJ&datatype=csv"
    )


def get_crypt_csv(key1="BTC", key2="USD"):
    return pd.read_csv(
        "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol="
        + key1
        + "&market="
        + key2
        + "&apikey=X01AA6ACSC2VWDLJ&datatype=csv"
    )


def put_chart(df, x, y, color):
    fig = px.line(df, x=x, y=y, color_discrete_sequence=[color])
    st.write(fig)


def put_table(df):
    st.dataframe(df, width=900)


ac = st.selectbox("Select your Asset Class", ["Forex", "Crypto"])

if ac == "Forex":
    ch = st.selectbox("Select your currency", ["USD", "EUR", "SGD"])
    if os.path.isfile(ac + ch + ".csv"):
        df = pd.read_csv(ac + ch + ".csv")
    else:
        df = get_fx_csv(ch)
       # df=pd.read_csv('forex.csv')
        print("pulling")
        time.sleep(3)
        df.to_csv(ac + ch + ".csv", index=False)
else:
    ch = st.selectbox("Select your crypto", ["BTC", "SHIB", "DOGE"])
    if os.path.isfile(ac + ch + ".csv"):
        df = pd.read_csv(ac + ch + ".csv")
    else:
        df = get_crypt_csv(ch)
        #df=pd.read_csv('crypto.csv')
        print("pulling")

        time.sleep(3)
        df.to_csv(ac + ch + ".csv", index=False)

handle = st.empty()

#add block metrics


with handle.container():
    fig1, fig2 = st.columns(2)
    with fig1:
        target1 = st.selectbox("Metric:", df.columns, key=7777)
        mx_date=df.timestamp.max().split('-')
        min_date=df.timestamp.min().split('-')

        slider1=st.slider(
            "Date Start:",
            value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            format="YYYY-MM-DD",
            min_value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            max_value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            key=1234
            )
        slider2=st.slider(
            "Date End:",
            value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            format="YYYY-MM-DD",
            min_value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            max_value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            key=5678
            )
        try:
            min_idx=df.index[df.timestamp==str(slider1).split(' ')[0]].tolist()[0]
            mx_idx=df.index[df.timestamp==str(slider2).split(' ')[0]].tolist()[0]
        except:
            min_idx=df.index[df.timestamp==df.timestamp[np.random.randint(len(df)//2,len(df)-1)]].tolist()[0]
            mx_idx=df.index[df.timestamp==df.timestamp[np.random.randint(0,len(df)//2)]].tolist()[0]

        print(f'{min_idx},{mx_idx}')
        put_chart(df.iloc[mx_idx:min_idx,:], "timestamp", target1, "#7a67ee")
        put_table(df.iloc[mx_idx:min_idx,:])
    with fig2:
        target2 = st.selectbox("Metric:", df.columns, key=9999)
        mx_date=df.timestamp.max().split('-')
        min_date=df.timestamp.min().split('-')

        slider1=st.slider(
            "Date Start:",
            value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            format="YYYY-MM-DD",
            min_value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            max_value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            key=4567
            )
        slider2=st.slider(
            "Date End:",
            value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            format="YYYY-MM-DD",
            min_value=datetime(int(min_date[0]),int(min_date[1]),int(min_date[2])),
            max_value=datetime(int(mx_date[0]),int(mx_date[1]),int(mx_date[2])),
            key=9876
            )
        try:
            min_idx=df.index[df.timestamp==str(slider1).split(' ')[0]].tolist()[0]
            mx_idx=df.index[df.timestamp==str(slider2).split(' ')[0]].tolist()[0]
        except:
            min_idx=df.index[df.timestamp==df.timestamp[np.random.randint(len(df)//2,len(df)-1)]].tolist()[0]
            mx_idx=df.index[df.timestamp==df.timestamp[np.random.randint(0,len(df)//2)]].tolist()[0]

        print(f'{min_idx},{mx_idx}')
        put_chart(df.iloc[mx_idx:min_idx,:], "timestamp", target2, "#ff0000")
        put_table(df.iloc[mx_idx:min_idx,:])
