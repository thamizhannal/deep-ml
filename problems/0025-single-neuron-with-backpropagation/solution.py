import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here

	weights = initial_weights
	bias = initial_bias
	mses = []

	for _ in range(epochs):
		z = np.dot(features, weights) + bias
		predictions = 1/ ( 1 + np.exp(-z))
		num_of_samples = features.shape[0]
		errors = predictions - labels
		mse_value =  np.mean(errors ** 2)
		mses.append(round(mse_value, 4))

		# grad computation
		weights_grads = (2/num_of_samples) * np.dot(features.T, errors*predictions*(1-predictions))  
		bias_grads = (2/num_of_samples) * np.sum(errors*predictions*(1-predictions))

		# weight and bias updates
		weights -= learning_rate * weights_grads
		bias -= learning_rate * bias_grads

	return np.round(weights,4), np.round(bias,4), mses