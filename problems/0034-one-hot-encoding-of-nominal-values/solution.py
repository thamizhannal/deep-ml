import numpy as np
from sklearn.preprocessing import OneHotEncoder

def to_categorical(x, n_col=None):
	# Your code here
	target_x = np.array(x).reshape(-1,1)

	if n_col is not None:
		categories = [list(range(n_col))]
		encoder = OneHotEncoder(categories= categories, sparse_output=False) 
	else:
		encoder = OneHotEncoder(sparse_output=False)
	
	return encoder.fit_transform(target_x)