import numpy as np
import matplotlib.pyplot as plt
def sig(x):
    return 1/(1+ np.exp(x))*255

def plot():
    x = np.linspace(-10,10,50)
    p = sig(x)
    plt.xlabel("x")
    plt.ylabel("Sigmoid(x)")
    plt.plot(x,p)
    plt.show()

plot()