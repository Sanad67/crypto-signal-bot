


def run_backtest(df, signals):
    # your existing capital/crypto/fee loop
    # but reading from `signals` (the parameter), not recomputing

    capital = 10000
    crypto = 0 
    fee_rate = 0.001

    for index, value in signals.items():
        row_pos = signals.index.get_loc(index)
        if row_pos + 1 < len(signals):
            fill_price = df['Price'].iloc[row_pos + 1]
            if (value == 1) and (crypto == 0):
                capital = capital * (1-fee_rate)
                crypto = capital/ fill_price
                capital = 0
            if (value ==  -1) and (crypto > 0):
                capital = crypto * fill_price * (1 - fee_rate)
                crypto = 0

    last_price = df['Price'].iloc[-1]
    if crypto > 0:
        capital = crypto * last_price * (1 - fee_rate)
        crypto = 0 

    return capital