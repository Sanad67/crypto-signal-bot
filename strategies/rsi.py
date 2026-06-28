from strategies.base import Strategy

class RSIStrategy(Strategy):
    def __init__(self, period=14):
        self.period = period


    @property
    def name(self) -> str:
        return "RSI"
    
    def generate_signals (self, data):
        return
