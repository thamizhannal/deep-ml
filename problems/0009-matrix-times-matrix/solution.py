import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              mat_A = np.array(a)
              mat_B = np.array(b)
              A_row, A_col = mat_A.shape[0], mat_A.shape[1]
              B_row, B_col = mat_B.shape[0], mat_B.shape[1]
              if A_col == B_row:
                return np.matmul(mat_A, mat_B).tolist()
              return -1