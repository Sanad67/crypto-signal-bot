from strategies.base import Strategy
import pandas as pd
import numpy as np

class MACrossover(Strategy):

    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window


    @property
    def name(self) -> str:
        return "MA Crossover"


    def generate_signals (self, data):

        #Moving average 
        data['MA_short'] = data['Price'].rolling(window = self.short_window).mean()
        data[ 'MA_long'] = data['Price'].rolling(window= self.long_window).mean()
        data['price_diff'] = data['MA_short'] - data['MA_long']
        data['diff_prev'] = data['price_diff'].shift(1)

        #Signal data 
        data['Signal'] = 0
        data.loc[(data['diff_prev'] <= 0) & (data['price_diff'] > 0), 'Signal'] = 1
        data.loc[(data['diff_prev'] >= 0) & (data['price_diff'] < 0), 'Signal'] = -1

        return data['Signal']
