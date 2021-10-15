def option_p_and_l(option, closing_price):
    if option['type'] == 'call':
        if closing_price < option['strike_price']:
            return option['call_price'] * option['lot_size']
        else:
            return (closing_price - (option['strike_price'] - option['call_price'])) * option['lot_size']
        
    else:
        if closing_price < option['strike_price']:
            return (option['strike_price'] + option['call_price'] - closing_price) * option['lot_size']
        else:
            return option['call_price'] * option['lot_size']

def stock_p_and_l(stock, closing_price):
    return (closing_price - stock['cmp']) * stock['lot_size']