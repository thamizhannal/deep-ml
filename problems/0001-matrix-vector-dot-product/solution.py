def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	import numpy as np
	mat_a = np.array(a)
	mat_b = np.array(b)

	len_a = np.shape(mat_a)[0]
	row_a, col_a = np.shape(mat_a)[0], np.shape(mat_a)[1]
	
	len_b = np.shape(b)[0]

	if col_a != len_b:
		return -1
	
	return np.dot(a, b).tolist()