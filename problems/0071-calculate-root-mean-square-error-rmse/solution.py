
import numpy as np
import math
def rmse(y_true, y_pred):
    # Write your code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")

    if y_true.size == 0:
        raise ValueError("Arrays cannot be empty")

    if not np.all(np.isfinite(y_true)) or not np.all(np.isfinite(y_pred)):
        raise ValueError("Arrays must contain finite values")
    total = np.mean((y_true-y_pred)**2)
    rmse_res = np.sqrt(total)
    return round(rmse_res,3)
