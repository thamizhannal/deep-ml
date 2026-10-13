import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    train_mean = np.mean(X_train, axis=0)
    train_sd = np.std(X_train, axis=0)
    train_sd[train_sd==0]=1

    test_z = (X_test - train_mean)/train_sd
    return test_z
    
