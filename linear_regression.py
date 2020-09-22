import os
import numpy as np
from matplotlib import pyplot

def cost(theta, y, X):
	n = y.size
	prediction = np.sum(np.square(y - np.inverse(theta[1:])*X + theta[0]))/

def gradient_descent():
	return 1

def predict():
	return 1

def main():
	#load data
	data = np.genfromtxt(os.path.join('Data', 'winequality-white.csv'), delimiter=';')
	X, y = data[:, :11], data[:, 11:]
	print(y.shape)



if __name__ == "__main__":
    main()