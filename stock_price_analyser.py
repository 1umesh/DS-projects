import pandas as pd
import streamlit as st
import yfinance as yf
import datetime




st.title(
    """
    STOCK
    """
)

ticker_symbol=st.text_input("enter symbol","MSFT",key="placeholder")

col1,col2 =st.columns(2)

with col1:
    start_date=st.date_input("Enter Starting date",datetime.date(2019,1,1))
with col2:
    end_date=st.date_input("Enter end date",datetime.date(2022,12,31))

ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")
st.dataframe(ticker_df)
#graph for daily closing price 
st.write(""" # daily closing price chart""")
st.line_chart(ticker_df.Close)
#graph for daily volume trades price 
st.write(""" # daily trade volume chart""")
st.line_chart(ticker_df.Volume)