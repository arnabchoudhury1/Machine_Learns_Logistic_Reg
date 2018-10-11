import pylab
import numpy as np
import pandas as pd
import math


df = pd.read_csv("testdata.csv", usecols = [0, 0])
x1 = df.values
print(x1)
input("Enter to continue")

df = pd.read_csv("testdata.csv", usecols = [1, 1])
x2 = df.values
print(x2)
input("Enter to continue")

df = pd.read_csv("testdata.csv", usecols = [2, 2])
y = df.values
print(y)
input("Enter to continue")

df = pd.read_csv("testdata.csv", usecols = [0,1])
X = df.values
print(X)

m = X.shape[0]
print(m)
input("Enter to continue")



def sigmoid(theta, X):
		#theta = np.zeros(shape=X.shape)
		
		den = 1 + np.exp(-np.dot(np.transpose(theta),X))
		
		sig = 1/den
		
		return sig
theta = np.zeros(shape=X.shape)
#print(sigmoid(theta, X, y))
def cost_func(theta, X, y):
	J = -1/m*(np.dot(np.transpose(y), np.log(sigmoid(theta, X)))+np.dot(np.transpose(1-y), np.log(1-sigmoid(theta, X))))
	#grad = np.transpose((1./m)*np.transpose(sigmoid(np.dot(theta, X))-y).dot(X)
	
	return J
print(cost_func(theta, X, y))	

	
	
	