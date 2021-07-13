import numba
import numpy as np
import math
import matplotlib.pyplot as plt

def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    print(type(a))
    if a > b:
        return a - b
    else:
        return a + b

if __name__ == "__main__":    
    vfunc = np.vectorize(myfunc)
    print(vfunc([1, 2, 3, 4], 2))
    print(vfunc.__doc__)
    #myfunc(np.array([1, 2, 3, 4]), 2)
    #print(myfunc(np.array([1, 2, 3, 4]), 2))
