#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import preprocessing


# In[2]:


gain = lambda x: x if x > 0 else 0 # works as a map function or in list comprehension
loss = lambda x: abs(x) if x < 0 else 0 # works as a map function or in list comprehension
# Relative Strength Index 
def rsi(crypto):    
    # Create a list, fill first 14 values with 'None'
    rsi_list = [None for i in range(14)]
    # Change as an input
    crypro = crypto.Change
    
    # Calculating first RSI
    avg_gain = sum([i for i in crypto[1:15] if i > 0])/14
    avg_loss = sum([abs(i) for i in crypto[1:15] if i < 0])/14
    rs = avg_gain / avg_loss
    rsi = 100 - ( 100 / ( 1 + rs ))
    rsi_list.append(rsi)
    
    # Calculating following RSI's
    for i in range(15, len(crypto)):
        avg_gain = (avg_gain * 13 + gain(crypto[i]))/14
        avg_loss = (avg_loss * 13 + loss(crypto[i]))/14
        rs = avg_gain / avg_loss
        rsi = 100 - ( 100 / ( 1 + rs ))
        rsi_list.append(rsi)
    
    return rsi_list   
 
# Moving Average Convergence/Divergence        
def macd(crypto):
    exp1 = stock.Close.ewm(span=12, adjust=False).mean()
    exp2 = stock.Close.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
 
# Bollinger Bands    
def bollinger_bands(crypto, window=21):
    rolling_mean = crypto.Close.rolling(window).mean()
    rolling_std = crypto.Close.rolling(window).std()
    upper_band = rolling_mean + (rolling_std*2)
    lower_band = rolling_mean - (rolling_std*2)
    return upper_band, lower_band
 
# Moving Average (7 days period)    
def ma7(crypto):
    return crypto.Close.rolling(7).mean()
  
# Moving Average (21 days period)  
def ma21(crypto):
    return crypto.Close.rolling(21).mean()
    
def momentum(data, n_days):
    m = [None for i in range(n_days)]    
    for i in range(len(data) - n_days):
        end = i + n_days
        m.append(data[i] - n_days)
    return m


# In[ ]:




