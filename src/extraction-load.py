# Importing Libraries

import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Importing enviornment variables

symbols = ["GC=F", "SI=F", "CL=F", "BZ=F", "ZS=F", "KC=F"]

def fetch_df(symbol, period="2y", interval="1d"):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)[["Close"]]
    df["symbol"] = symbol
    return df


if __name__== "__main__":
    
    all_data = []
    for symbol in symbols:
        df = fetch_df(symbol)
        all_data.append(df)

    final_df = pd.concat(all_data)
    print(final_df)