import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
  
    n_col = np.max(x)+1 if n_col is None else n_col
    arr = [[0 for j in range(n_col)] for i in range(len(x))]
    for i in range(len(x)):
        arr[i][x[i]]  = 1
    arr = np.asarray(arr)
    return arr