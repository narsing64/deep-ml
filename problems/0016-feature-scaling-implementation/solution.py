import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    n,d = data.shape
    variance = np.var(data,axis=0)
    sigma = np.sqrt(variance)
    means = np.mean(data,axis=0)
    standardized_data = (data-means)/sigma
    mins = np.min(data,axis = 0)
    maxs = np.max(data,axis =0)
    normalized_data = (data-mins)/(maxs-mins)
    return standardized_data, normalized_data