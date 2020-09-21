import os
import numpy as np
from matplotlib import pyplot

def load_data():
	data = np.loadtxt(os.path.join('Data', 'winequality-white.csv'), delimiter=',')
	X, y = data[1:, 0], data[1:, 1]

	m = y.size 
	print(y.size())

def main():
	load_data()

if __name__ == "__main__":
    main()