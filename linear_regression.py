import os
import numpy as np
from matplotlib import pyplot

def load_data():
	data = np.genfromtxt(os.path.join('Data', 'winequality-white.csv'), delimiter=';')
	X, y = data[:, :11], data[:, 11:]
	print(y.shape)

def cost():

def gradient_descent():

def predict:

def main():
	load_data()

if __name__ == "__main__":
    main()