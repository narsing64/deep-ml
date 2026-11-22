
import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    total = np.sum(y_pred)
    avg = total/len(y_pred)
    sst = 0
    for num in y_true:
        sst += (num-avg)*(num-avg)
    ssr = 0
    for i in range(len(y_pred)):
        ssr += (y_pred[i]-y_true[i])*(y_pred[i]-y_true[i])
    
    ssr1 = np.sum((y_pred-y_true)**2)
    sst1 = np.sum((y_true-avg)**2)
    
    return 1-ssr1/sst1
