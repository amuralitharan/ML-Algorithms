import os
import numpy as np
from matplotlib import pyplot

def cost(theta, y, X):
	n = y.size
	prediction = np.sum(np.square(y - np.transpose(theta[1:])*X + theta[0]))/n
	print(prediction.shape)

def gradient_descent():
	return 1

def predict():
	return 1

def main():
	#load data
	data = np.genfromtxt(os.path.join('Data', 'winequality-white.csv'), delimiter=';')
	X, y = data[:, :11], data[:, 11:]

	#generate sample theta
	theta = np.random.rand(12)
	cost(theta, y, X)

if __name__ == "__main__":
    main()