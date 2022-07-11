#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys                      
from PyQt5.QtWidgets import *   
from PyQt5 import uic           
from PyQt5.QtCore import *
import pybithumb

form_class=uic.loadUiType("day04.ui")[0] 
tickers = ["BTC","ETH","XRP","ADA"]

class MyWindow(QMainWindow, form_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)
    
    def timeout(self):
        for i, ticker in enumerate(tickers):
            
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i,0, item)
            
            price = QTableWidgetItem(str(pybithumb.get_current_price(ticker)))
            self.tableWidget.setItem(i,1, price)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()




