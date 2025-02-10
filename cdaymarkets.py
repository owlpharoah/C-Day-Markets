import streamlit as st
import pandas as pd
import yfinance as yf


st.set_page_config(layout="wide")

background_url = "https://img.freepik.com/free-vector/abstract-infinity-wireframe-layout-graphic-design_1017-47103.jpg"
# Background
st.markdown(
    f"""
    <style>
        .stApp {{
            background: url("{background_url}") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: #FFD700; font-size:130px;'>C-Day Markets</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #EAEAEA;'>Stocks Post Covid</h3>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #ADD8E6;'>(March 11, 2020)</h6>", unsafe_allow_html=True)
st.divider()

c1,c2,c3,c4= st.columns(4,border=True,vertical_alignment="top")


with c1:
    st.markdown('<h2 style="color: yellow;">Popular ⭐</h2>', unsafe_allow_html=True)
    st.divider()
    st.header("Reliance")
    ticker_name = ('RELIANCE.NS')
    ticker = yf.Ticker(ticker_name)

    hisd = ticker.history(start="2020-03-11",interval="1d")
    hisdata = {"Average": (hisd["High"]+hisd["Low"])/2}
    df = pd.DataFrame(hisdata)


    st.line_chart(df,x_label='Months',y_label='Average Price')
    st.divider()
    st.header("SBI")
    ticker_name2 = ('SBIN.NS')
    ticker2 = yf.Ticker(ticker_name2)

    hisd2 = ticker2.history(start="2020-03-11",interval="1d")
    hisdata2 = {"Average": (hisd2["High"]+hisd2["Low"])/2}
    df2 = pd.DataFrame(hisdata2)

    st.line_chart(df2,x_label='Months',y_label='Average Price')

with c2:
    st.markdown('<h2 style="color: red;">Highly Affected🚩</h2>', unsafe_allow_html=True)
    st.divider()
    st.header("IndusInd Bank")
    ticker_name3 = ('INDUSINDBK.NS')
    ticker3 = yf.Ticker(ticker_name3)

    hisd3 = ticker3.history(start="2020-03-11",interval="1d")
    hisdata3 = {"Average": (hisd3["High"]+hisd3["Low"])/2}
    df3 = pd.DataFrame(hisdata3)

    st.line_chart(df3,x_label='Months',y_label='Average Price')
    st.divider()

    st.header("Eicher Motors")
    ticker_name4 = ('EICHERMOT.NS')
    ticker4 = yf.Ticker(ticker_name4)

    hisd4 = ticker4.history(start="2020-03-11",interval="1d")
    hisdata4 = {"Average": (hisd4["High"]+hisd4["Low"])/2}
    df4 = pd.DataFrame(hisdata4)

    st.line_chart(df4,x_label='Months',y_label='Average Price')


with c3:
    st.markdown('<h2 style="color: green;">High Growth🏆</h2>', unsafe_allow_html=True)
    st.divider()
    st.header("Zomato ")
    ticker_name5 = ('ZOMATO.NS')
    ticker5 = yf.Ticker(ticker_name5)

    hisd5 = ticker5.history(start="2020-03-11",interval="1d")
    hisdata5 = {"Average": (hisd5["High"]+hisd5["Low"])/2}
    df5 = pd.DataFrame(hisdata5)

    st.line_chart(df5,x_label='Months',y_label='Average Price')
    st.divider()

    st.header("Aurobindo Pharma")
    ticker_name6 = ('AUROPHARMA.NS')
    ticker6 = yf.Ticker(ticker_name6)

    hisd6 = ticker6.history(start="2020-03-11",interval="1d")
    hisdata6 = {"Average": (hisd6["High"]+hisd6["Low"])/2}
    df6 = pd.DataFrame(hisdata6)

    st.line_chart(df6,x_label='Months',y_label='Average Price')


with c4:
    st.markdown('<h2 style="color: DodgerBlue;">Recovering🩹</h2>', unsafe_allow_html=True)
    st.divider()
    st.header("Jet Airways")
    ticker_name7 = ('JETAIRWAYS.NS')
    ticker7 = yf.Ticker(ticker_name7)

    hisd7 = ticker7.history(start="2020-03-11",interval="1d")
    hisdata7 = {"Average": (hisd7["High"]+hisd7["Low"])/2}
    df7 = pd.DataFrame(hisdata7)

    st.line_chart(df7,x_label='Months',y_label='Average Price')
    st.divider()

    st.header("Vodafone Idea")
    ticker_name8 = ('IDEA.NS')
    ticker8 = yf.Ticker(ticker_name8)

    hisd8 = ticker8.history(start="2020-03-11",interval="1d")
    hisdata8 = {"Average": (hisd8["High"]+hisd8["Low"])/2}
    df8 = pd.DataFrame(hisdata8)

    st.line_chart(df8,x_label='Months',y_label='Average Price')


