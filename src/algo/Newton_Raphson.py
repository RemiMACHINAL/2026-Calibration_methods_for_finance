from typing import Callable

def Newton_Raphson(f:Callable, df:Callable, x0:float, tol:float=1e-9, max_iter:int=1000) -> float:
    """
    Newton_Raphson algorithm template to find functionn f zero.
    Require :   f, the function to which zero is to find
                df, derivative to f
                x0, starting point
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)         
        if abs(fx) < tol:
            return x
        x -= fx / df(x) 
    raise ValueError(f"ERR : In Newton_Raphson, impossible to converge after {max_iter} iterations.")