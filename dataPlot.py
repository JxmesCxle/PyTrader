import plotly.graph_objs as go
import numpy as np
import pandas as pd
import menu
import os

#STOCK MARKET DATA SOURCE
import yfinance


def createGraph(tickerBoxValue, tickerPeriod, tickerInterval):

    #declare figure
    fig = go.Figure()


    dataTicker = yfinance.Ticker(tickerBoxValue)
    history = dataTicker.history(period="1y")

    #Candlestick
    fig.add_trace(go.Candlestick(x=history.index,
            open=history['Open'],
            high=history['High'],
            low=history['Low'],
            close=history['Close'], name = 'market data'))
        
        
    # Add titles
    fig.update_layout(
        title= f"{tickerBoxValue} live share price evolution",
        yaxis_title = f"Stock Price (USD per Shares)")

        
    if not os.path.exists("graphs"):
        os.mkdir("graphs")

    filename = str(tickerBoxValue+".jpeg")
    fig.write_image("graphs/" + filename, width=650, height=450, scale=2)

    #fig.show()





