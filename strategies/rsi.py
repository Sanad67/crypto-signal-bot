from strategies.base import Strategy

class RSIStrategy(Strategy):
    def __init__(self, period=14):
        self.period = period


    @property
    def name(self) -> str:
        return "RSI"
    
    def generate_signals (self, data):
        # Calculate average gain and loss
        # this is for the average gain and loss 
        data['delta'] = data['Price'].diff() 
        data['gain'] = 0.0
        data['loss'] = 0.0 
        data.loc[(data['delta'] > 0) , 'gain'] = data['delta']
        data.loc[(data['delta'] < 0) , 'loss'] = data['delta'].abs()

        avg_gain = data['gain'].rolling(window=self.period).mean()
        avg_loss = data['loss'].rolling(window=self.period).mean()
        rs = avg_gain / avg_loss
        data['RSI'] = 100 - (100 / (1 + rs))

        data['Signal'] = 0
        data.loc[(data['RSI'] >=70 ), 'Signal'] = -1
        data.loc[(data['RSI'] <=30 ), 'Signal'] =  1
        
        return data["Signal"]