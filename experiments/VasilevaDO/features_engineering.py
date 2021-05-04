
import pandas as pd
from sklearn import preprocessing

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
    exp1 = crypto.Close.ewm(span=12, adjust=False).mean()
    exp2 = crypto.Close.ewm(span=26, adjust=False).mean()
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
    
def momentum2(data, n_days):
    m = [None for i in range(n_days)]    
    for i in range(len(data) - n_days):
        end = i + n_days
        m.append(data[i] - n_days)
    return m


def relativeStrengthIndex(data, num):
    if not isinstance(data, dict):
        raise Exception('Dictionary input expected')
    if not isinstance(num, int):
        raise Exception('Integer input expected')
    if num < 7 or num > 21:
        raise Exception('Unusual numeric input detected')
    if (num > len(data)):
        raise Exception('Insufficient data for calculation')
    data_keys=list(data.keys())
    data_list=list(data.values())
    result = {}
    last_price = -1
    gains_losses_list = []
    for x in range(len(data_list)):
        if (last_price != -1):
            diff = round((data_list[x] - last_price), 2)
            
            if (diff > 0):
                gains_losses = [ data_list[x], diff, 0 ]
            elif (diff < 0):
                gains_losses = [ data_list[x], 0, abs(diff) ]
            else:
                gains_losses = [ data_list[x], 0, 0 ]
            
            gains_losses_list.append(gains_losses)
        sum_gains = 0
        sum_losses = 0
        avg_gains = 0
        avg_losses = 0 
        if (x == num):
            series = gains_losses_list[-num::]
        
            for y in series:
                sum_gains += y[1]
                sum_losses += y[2]
            avg_gains = sum_gains / num
            avg_losses = sum_losses / num
            rs = avg_gains / avg_losses
            rsi = 100 - (100 / (1 + rs))
            last_gain_avg = avg_gains
            last_loss_avg = avg_losses
            result[data_keys[x]] = round(rsi, 2)
        if (x > num):
            current_list = gains_losses_list[-1::]
            current_gain = current_list[0][1]
            current_loss = current_list[0][2]
            current_gains_avg = (last_gain_avg * (num - 1) + current_gain) / num
            current_losses_avg = (last_loss_avg * (num - 1) + current_loss) / num
            rs = current_gains_avg / current_losses_avg
            rsi = 100 - (100 / (1 + rs))
            last_gain_avg = current_gains_avg
            last_loss_avg = current_losses_avg
            result[data_keys[x]] = round(rsi, 2)    
      
        last_price = data_list[x]
    return result




