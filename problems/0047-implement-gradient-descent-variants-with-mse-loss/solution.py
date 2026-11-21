import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    m,n = X.shape
    y = y.reshape(-1,1)
    weights = weights.reshape(-1,1)
    if method=='batch':
        batch_size = m 
    for epoch in range(n_epochs):
        for i in range(0,m,batch_size):
            temp = X[i:i+batch_size]
            temp_y = y[i:i+batch_size]
            cal = temp@weights-temp_y
            loss = 2*(temp.T@cal)/(len(temp))
            weights = weights-learning_rate*loss
    return weights.flatten()
    

