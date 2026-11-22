import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    sigma = np.std(X_train,axis = 0)
    means = np.mean(X_train,axis = 0)
  #  scaler = (X_train-means)/sigma
   # scaler_sigma = np.std(scaler,axis = 0)
    #scaler_mean = np.mean(scaler,axis = 0)
    
    sigma = np.where(sigma==0,1,sigma)
    ans = (X_test-means)/sigma
    return ans
