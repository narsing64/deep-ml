import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n,d = data.shape
    #shuffle
    rng = np.random.default_rng(seed)
    data = rng.permutation(data)
    train_end = int(n*train_frac)
    val_end = int(train_end + int(n*validation_frac))
    train = data[:train_end,:]
    val = data[train_end:val_end,:]
    test = data[val_end:,:]
    return [train,val,test]