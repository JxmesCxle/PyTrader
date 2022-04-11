#GUI PACKAGES
from re import A
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from numpy.lib.function_base import quantile

#STOCK MARKET DATA SOURCE
import yfinance as yf


#DATA VISUALISATION
import plotly.graph_objs as go

#DATA VISUALISTAION SCRIPT
import dataPlot


import numpy as np
import pandas as pd
import sys
import os




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Python Trading Analyser'
        self.size = [10,10,400,140]
        self.components()

        self.interval = "1m"
        self.period = "1d"

        self.show()
        self.showMaximized()
    
    def components(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.size[0],self.size[1],self.size[2],self.size[3])
    

        #--------------------------- MENU WIDGETS ------------------------#

       
       
        #---- TICKER TEXTBOX ----#
        
        self.tickerBox = QLineEdit(self)
        self.tickerBox.move(20, 25)
        self.tickerBox.resize(60,30)

        self.tickerLabel = QLabel(self)
        self.tickerLabel.setText("TICKER")
        self.tickerLabel.move(30,0)
      
        #---- END TICKER TEXTBOX ----#

        #---- INTERVAL DROPDOWN ----# 

        #OPTIONS
        intervalDropdown = QComboBox(self)
        intervalDropdown.addItem("1 minute")
        intervalDropdown.addItem("15 minutes")
        intervalDropdown.addItem("1 hour")
        intervalDropdown.addItem("1 day")
        intervalDropdown.addItem("1 week")

        intervalDropdown.move(100,25)

        #LINKS OPTION TO METHOD
        intervalDropdown.activated[str].connect(self.intervalChange)    


        #---- END INTERVAL DROPDOWN ----# 




        #---- GRAPH STEUP ----#

        #Graph label
        self.graphLabel = QLabel(self)
        self.graphLabel.move(20,120)
        self.graphLabel.resize(2000,1000)
        #---- END GRAPH STEUP ----#

        #---- CURRENT UNIT PRICE ----#
        self.unitPrice = QLabel(self)
        self.unitPrice.move(20,100)

        #---- END CURRENT UNIT PRICE ----#


        # Create a button in the window
        self.button = QPushButton('FIND', self)
        self.button.move(220,25)
        self.button.resize(60,30)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)


    def intervalChange(self, text):
        
        if text == "1 minute":
            self.interval = "1m"
            self.period = "1h"

        elif text == "5 minutes":
            self.interval = "5m"
            self.period = "1d"

        elif text == "15 minutes":
            self.interval = "15m"
            self.period = "5d"

        elif text == "1 hour":
            self.interval = "1h"
            self.period = "1wk"

        elif text == "1 day":
            self.interval = "1d"
            self.period = "1mo"

        elif text == "1 week":
            self.interval = "1wk"
            self.period = "3mo"

    
    @pyqtSlot()
    def on_click(self):
        tickerBoxValue = self.tickerBox.text()
        tickerPeriod = self.period
        tickerInterval = self.interval
        #self.tickerBox.setText("")

        #TICKER DATA SCRAPER
        #stockData = yf.download(tickers=tickerBoxValue, period='1d', interval='1m')
        #stockHistory = str(stockData.history(period='1d', start='2022-1-1', end='2022-1-25'))

        
        #Calls upon graph script to create graph image and saves it as a jpeg to "/graphs" folder
        dataPlot.createGraph(tickerBoxValue, tickerPeriod, tickerInterval)

        a = yf.Ticker(tickerBoxValue)
        
        self.unitPrice.setText("UNIT PRICE: " + str(a.info['regularMarketPrice']))
        
        #declares graph file
        graphFile = str(tickerBoxValue + ".jpeg")

        #creates the pixmap
        self.graph = QPixmap("./graphs/"+graphFile)
        
        #sets image to graph label
        self.graphLabel.setPixmap(self.graph)





        #changes ticker data
       # self.tickerData.setText(str(stockData))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())