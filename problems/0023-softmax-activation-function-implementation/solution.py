import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    import numpy as np
    X = np.array(scores)
    max_X = max(X)
    softmax = (np.exp(X - max_X)) /np.sum(np.exp(X-max_X))
    return softmax.tolist()