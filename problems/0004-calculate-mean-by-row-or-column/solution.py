def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	A = np.array(matrix)
	if mode in "row":
		return np.mean(A, axis=1)
	return np.mean(A, axis=0)