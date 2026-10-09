import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	mat_A = np.array(a)
	mat_A_shape = np.shape(mat_A)

	if not new_shape:
		return []

	mat_A_row, mat_A_col = mat_A_shape[0], mat_A_shape[1]

	mat_B = np.array(new_shape)
	#mat_B_shape = np.shape(mat_B)
	#mat_B_row, mat_B_col = mat_B_shape[0], mat_B_shape[1]

	if (mat_A_col*mat_A_row) == (new_shape[0]*new_shape[1] ) :
		reshaped_A = mat_A.reshape(new_shape).tolist()
		return  reshaped_A



	return []