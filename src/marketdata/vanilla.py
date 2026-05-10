from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

def Get_Div_and_Spot_from_Vanilla(Call_prices:dict[float,dict[float,float]], Puts_prices:dict[float,dict[float,float]], Rate:dict[float,float]) -> tuple[float, float]:
    """
    Extracting S spot and q dividende rate from observed vanilla prices;
    Expect data key : vanillas maturity,
                value : dict    key : K strike
                                value : mid price
            rate : dict with value rate corresponding to maturity key T
    """
    if Call_prices.keys() != Puts_prices.keys():
        raise TabError("ERR : In Get_Div_and_Spot_from_Vanilla, Calls and Puts maturities do not match.")
    if len(Call_prices.keys()) != len(Rate):
        raise TabError(f"ERR : In Get_Div_and_Spot_from_Vanilla, Rate and Maturity length do not match, {len(Call_prices.keys())} and {len(Rate)}.")
    
    t_s_w_div = []
    for T in Call_prices.keys():
        if Call_prices[T].keys() != Puts_prices[T].keys():
            raise TabError(f"ERR : In Get_Div_and_Spot_from_Vanilla, Calls and Puts strikes do not match for maturity {T}.")
        nb_obs = len(Call_prices[T].keys())
        s_w_div = 0
        for k in Call_prices[T].keys():
            s_w_div += Call_prices[T][k] - Puts_prices[T][k] + np.exp(-Rate[T]*T)*k
        t_s_w_div.append(np.log(s_w_div/nb_obs))

    model = LinearRegression()
    model.fit(np.array(list(Call_prices.keys())).reshape(-1, 1), t_s_w_div)
    return (np.exp(model.intercept_), -model.coef_[0])
