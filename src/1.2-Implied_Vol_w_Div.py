import pandas as pd
import numpy as np
from marketdata.vanilla import Get_Div_and_Spot_from_Vanilla
from display.graphs import Display_From_f_w_Two_Variable
from instruments.BS_Options import Implied_Vol



df = pd.read_csv("data/sp-index.txt",
        sep='\t',
        index_col=False,
		header=0
	)

# Formating data
dict_c = {}
dict_p = {}
dict_rate = {}
for t in np.unique(df["T"]):
    temp_dict_c = {}
    temp_dict_p = {}
    for k in np.array(df[df["T"]==t]["K"]):
        temp_dict_c[k] = ( df[(df["T"]==t) & (df["K"]==k)]["Cb"] + df[(df["T"]==t) & (df["K"]==k)]["Ca"] ).iloc[0] /2
        temp_dict_p[k] = ( df[(df["T"]==t) & (df["K"]==k)]["Pb"] + df[(df["T"]==t) & (df["K"]==k)]["Pa"] ).iloc[0] /2
    dict_c[t] = temp_dict_c
    dict_p[t] = temp_dict_p
    dict_rate[t] = df[(df["T"]==t)]["r"].iloc[0]/100

s_0, q = Get_Div_and_Spot_from_Vanilla(dict_c, dict_p, dict_rate)


T = np.unique(df["T"])
for t in T :
    r = df[(df["T"]==t)]["r"].iloc[0]/100
    strike = list(dict_c[t].keys())
    price = list(dict_c[t].values())
    Display_From_f_w_Two_Variable(
        lambda x, var : Implied_Vol(s_0*np.exp(-q*t), x, r, t, var),
        strike,
        price,
        f"Skew sticky strike T={t}",
        x_label="Strike",
        y_label="Implied vol",
        save=True,
        save_name=f"res/1.2-Implied_Vol/Implied_vol_SP500_call_{np.round(t,2)}.png", 
        remove_zero=True)
