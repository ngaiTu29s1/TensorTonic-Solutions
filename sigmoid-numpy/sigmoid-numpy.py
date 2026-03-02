import numpy as np
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    return 1/(1+np.asarray(np.exp(-x, dtype = float)))