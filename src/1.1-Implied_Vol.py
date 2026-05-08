from display.graphs import *
from instruments.BS_Options import *


sigma=0.5
T=0.5
r=0.1
K=10

# Getting Call prices and Vega curves

Display_From_f_w_One_Variable(
    lambda x : Vanilla_BS(x, K, r, T, sigma),
    range(0,20),
    title="Call prices",
    x_label="Strike",
    y_label="Call price",
    save=True,
    save_name="res/1.1-Implied_Vol/Call_prices.png")
Display_From_f_w_One_Variable(
    lambda x : Vega_BS(x, K, r, T, sigma),
    range(0,20),
    "Vega",
    x_label="Strike",
    y_label="Vega value",
    save=True,
    save_name="res/1.1-Implied_Vol/Vega_values.png")

# Getting implied vol Skew

r=0.05
T=4/12
S0=5430.3
strike = [5125,5225,5325,5425,5525,5625,5725,5825]
price = [475,405,340,280.5,226,179.5,139,105]

# Getting implied vol Skew
 
Display_From_f_w_Two_Variable(
    lambda x, var : Implied_Vol(S0, x, r, T, var),
    strike,
    price,
    "Skew sticky strike",
    x_label="Strike",
    y_label="Implied vol",
    save=True,
    save_name="res/1.1-Implied_Vol/Implied_vol_LIFFE_data.png")






