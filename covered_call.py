# imports
import matplotlib.pyplot as plt
import p_and_l
import plot_graph



# Get inputs

cmp = float(input('Please enter the current market price of stock/index: '))
strike_price = float(input('Please enter the strike price for the call: '))
lot_size = float(input('Please enter the lot size of the call: '))
call_price = float(input('Please enter the call price per unit (not lot): '))

option = {
    'cmp': cmp,
    'type': 'call',
    'strike_price': strike_price,
    'lot_size': lot_size,
    'call_price': call_price
}

# Compute P&L equation in each region

# # Realized P&L
# def option_p_and_l(closing_price):
#     if closing_price <= strike_price:
#         return call_price * lot_size
#     else:
#         return -(closing_price - strike_price) * lot_size

# # def option_when_ends_below_strike_price(closing_price):
# #     return call_price * lot_size

# # def option_when_ends_above_strike_price(closing_price):
# #     return -(closing_price - strike_price) * lot_size

# # Unrealized P&L
# def stock_p_and_l(closing_price):
#     return (closing_price - cmp) * lot_size

# total P&L if stocks are sold when option in loss, else stocks are retained as book loss
def net_p_and_l(option, closing_price):
    if closing_price < option['strike_price'] + option['call_price']:
        return p_and_l.option_p_and_l(option, closing_price)
    else:
        return p_and_l.option_p_and_l(option, closing_price) + p_and_l.stock_p_and_l(option, closing_price)


x = list(range(int(0.7*cmp), int(1.3*cmp), 1))
y = [net_p_and_l(option, closing_price) for closing_price in x]

strike_price_xy = [strike_price, net_p_and_l(option, strike_price)]
cmp_xy = [cmp, net_p_and_l(option, cmp)]
breakeven_xy = [strike_price + call_price - 1, net_p_and_l(option, strike_price + call_price - 1)]
# Net P&L graph. T&C: If stocks are sold when option in loss, else stocks are retained as book loss
plot_graph.plot(x, y, strike_price_xy, cmp_xy, breakeven_xy)