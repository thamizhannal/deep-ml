import math

def sigmoid(z: float) -> float:
	#Your code here
	import numpy as np
	result = 1 / (1 + np.exp(-z))
	return result