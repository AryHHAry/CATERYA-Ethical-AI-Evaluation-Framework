import numpy as np
def reweighing(X, y, sensitive):
    unique, counts = np.unique(sensitive, return_counts=True)
    total = len(sensitive)
    weights = np.ones_like(sensitive, dtype=float)
    for u,c in zip(unique, counts):
        weights[sensitive==u] = total / (len(unique) * c)
    return weights
