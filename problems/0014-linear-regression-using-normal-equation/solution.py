import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_transpose = np.transpose(X)
	X_transpose_X = np.dot(X_transpose, X)
	X_transpose_X_inverse = np.linalg.inv(X_transpose_X)
	
	X_transpose_y = np.dot(X_transpose, y)

	theta = np.dot(X_transpose_X_inverse, X_transpose_y)

	return theta