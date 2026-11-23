import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    # Your code here
    y_true = y_true.reshape(-1,1)
    w = w.reshape(-1,1)
    prod = X@w
    val = np.mean((y_true-prod)**2)
    reg = alpha*(w.T@w)
    return (val + reg).item()