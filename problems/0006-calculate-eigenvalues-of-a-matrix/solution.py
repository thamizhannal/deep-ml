def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	matrix_A = np.array(matrix)
	trace = matrix_A[0][0]+matrix_A[1][1]
	det_A = (matrix_A[0][0] * matrix_A[1][1]) - (matrix_A[0][1] * matrix_A[1][0])
	#print(f"trace={trace}, detA={det_A}")

	factor1 =((trace)+np.sqrt( np.square(trace) - 4*det_A))/2
	factor2 = ((trace)-np.sqrt( np.square(trace) - 4*det_A))/2
	#print(f"factor1={factor1},factor2={factor2}")

	eigenvalues =[factor1, factor2]
	sorted(eigenvalues)
	return eigenvalues