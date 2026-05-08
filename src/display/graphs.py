import matplotlib.pyplot as plt
from typing import Callable

def Display_From_f_w_One_Variable(f:Callable, x:list, title:str="", x_label:str="", y_label:str="", save:bool=False, save_name:str="UNAMED.png"):
    """
    Plot a 2D graph of the function f
    """
    y = [f(arg) for arg in x]
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if save:
        plt.savefig(save_name)
    plt.show()


def Display_From_f_w_Two_Variable(f:Callable, x:list, var:list, title:str="", x_label:str="", y_label:str="", save:bool=False, save_name:str="UNAMED.png"):
    """
    Plot a 2D graph of the function f when 1 additionnal argument must be itered
    """
    if(len(x) != len(var)):
        raise ValueError(f"ERR : In Display_From_f_w_Two_Variable, the two lists have differents sizes {len(x)} and {len(var)}.")
    y = [f(x[i], var[i]) for i in range(0,len(x))]
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if save:
        plt.savefig(save_name)
    plt.show()