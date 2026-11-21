import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    x = np.array(X)
    y = np.array(y)
    a = x.T@x
    b = x.T@y
    a = np.linalg.inv(a)
    return a@b