import numpy as np
from math import sqrt, pi
from scipy.stats import norm
from algo.Newton_Raphson import Newton_Raphson



def Vanilla_BS(s_0:float, k_strike:float, r:float, T:float, sigma:float, side:str = 'C') -> float:
    """
    Compute Call or Put Black Scholes prices. 
    'side' to something different than 'C' will return Put price.
    """
    eps = 1e-15
    d1 = ( np.log(s_0/k_strike + eps) + (r+pow(sigma,2)/2)*T ) / (sigma*sqrt(T))
    d2 = ( np.log(s_0/k_strike + eps) + (r-pow(sigma,2)/2)*T ) / (sigma*sqrt(T))
    if side == 'C':
        return s_0*norm.cdf(d1) - k_strike*np.exp(-r*T)*norm.cdf(d2)
    else:
        return k_strike*np.exp(-r*T)*norm.cdf(-d2) - s_0*norm.cdf(-d1)
    

def Vega_BS(s_0:float, k_strike:float, r:float, T:float, sigma:float) -> float:
    """
    Compute Vega of a Black Scholes Vanilla option
    """
    eps = 1e-15
    d1 = ( np.log(s_0/k_strike + eps) + (r+pow(sigma,2)/2)*T ) / (sigma*sqrt(T))
    return s_0*sqrt(T/(2*pi))*np.exp(-pow(d1,2)/2)



def Implied_Vol(s_0:float, k_strike:float, r:float, T:float, market_value:float, tol=1e-4) -> float:
    """
    Return implied vol from Newton Raphson algo for a Black Scholes Call
    """
    sigma_0 = sqrt(2*abs( (np.log(s_0/k_strike) + r*T)/T ))                           # init sigma to assure cvg
    if max(s_0-k_strike*np.exp(-r*T),0) < market_value and market_value < s_0:      # assuring existence of such vol
        return Newton_Raphson(lambda x: Vanilla_BS(s_0=s_0, k_strike=k_strike, r=r, T=T, sigma=x) - market_value,
                               lambda x: Vega_BS(s_0=s_0, k_strike=k_strike, r=r, T=T, sigma=x), 
                               sigma_0,
                               tol)
    else:
        return 0