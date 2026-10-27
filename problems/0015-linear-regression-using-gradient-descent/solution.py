import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    for _ in range(iterations):
        # Calculate predictions (shape: m,)
        predictions = X.dot(theta)
        
        # Calculate the error vector (shape: m,)
        errors = predictions - y
        
        # Calculate the gradient (shape: n,)
        # Derived from the derivative of MSE loss: (1/m) * X^T * (X*theta - y)
        gradient = (1 / m) * X.T.dot(errors)
        
        # Update weights simultaneously
        theta = theta - alpha * gradient

    return theta.flatten()