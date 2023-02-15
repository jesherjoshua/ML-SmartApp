#!/usr/bin/python3

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

t=0
st.set_page_config("Analytical Dashboard", layout="wide",page_icon='💵')

# forex_daily
fx_url = "https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=INR&apikey=X01AA6ACSC2VWDLJ&datatype=csv"
# crypto_daily
crypt_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=X01AA6ACSC2VWDLJ&datatype=csv"


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
st.title("ML Smart App Live Dashboard")

# use cryptocur and countries as filters for your dashboard


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


def put_chart(df, x, y,color):
    fig = px.line(df, x=x, y=y,color_discrete_sequence=[color])
    st.write(fig)

def put_table(df):
    st.dataframe(df,width=900)

ac=st.selectbox("Select your Asset Class",['Forex','Crypto'])
if ac=='Forex':
    ch=st.selectbox("Select your currency",['USD','EUR','SGD'])
    #df=get_fx_csv(ch)
    target1='open'
    target2='close'
    df=pd.read_csv('forex.csv')
    time.sleep(1)
else:
    ch=st.selectbox("Select your crypto",['BTC','ETH','DOGE'])
    #df=get_crypt_csv(ch)
    target1='open (USD)'
    target2='close (USD)'
    df=pd.read_csv('crypto.csv')
    time.sleep(1)

handle=st.empty()


for i in range(t,len(df)-100):

    with handle.container():
        fig1,fig2=st.columns(2)
        with fig1:
            put_chart(df.iloc[i:i+40,:],'timestamp',target1,'#7a67ee')
            put_table(df.iloc[i:i+40,:])
        with fig2:
            put_chart(df.iloc[i:i+40,:],'timestamp',target2,'#ff0000')
            put_table(df.iloc[i:i+40,:])

    time.sleep(0.5)




