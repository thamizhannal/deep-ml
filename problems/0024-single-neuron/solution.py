import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	mat_X = np.array(features)
	mat_weights = np.array(weights)
	actual_lables = np.array(labels)

	z = np.dot(mat_X, mat_weights)+bias
	predictions = 1/(1+np.exp(-z))
	n = mat_X.shape[0]
	#predicted_labels = np.argmax(probabilities, axis=1)
	
	mse = np.mean((predictions-actual_lables) ** 2)
	
	return np.round(predictions, 4).tolist(), round(float(mse), 4)