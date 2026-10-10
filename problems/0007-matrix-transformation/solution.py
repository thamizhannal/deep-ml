import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)
	if det_S == 0 or det_T == 0:
		return -1

	inv_T=np.linalg.inv(T)
	mat_inv_T = np.array(inv_T)
	mat_A = np.array(A)

	mat_S = np.array(S)
	
	mat_mul = np.matmul(mat_inv_T, mat_A)
	transformed_matrix = np.matmul(mat_mul, mat_S)

	return transformed_matrix