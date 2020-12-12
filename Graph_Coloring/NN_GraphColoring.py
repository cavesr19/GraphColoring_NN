#CSC 301 Final Project Sebastian Cave and Rafael Marquez
#Based off of the structures from Michael Nielsen's book:
#http://neuralnetworksanddeeplearning.com/chap1.html
#12/10/2020

import numpy as np
import random

class Network(object):
	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

	def feedforward(self, a):
		for b, w in zip(self.biases, self.weights):
			a = sigmoid(np.dot(w, a) + b)
		return a

def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):


#Sigmoid Functions
def sigmoid(z):
	return 1 / (1 + np.exp(-z))

net = Network([2, 2, 2])
print net.sizes
print net.biases
print net.weights
