# Grupo 33 : Mariana -> 83520 : Carlos -> 81395
import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    
    reg = KernelRidge(kernel='rbf', gamma=0.1,alpha=0.001)
    #reg = KernelRidge(kernel='polynomial', degree=6)
    mytrainingaux(X,Y,reg)
    
    return reg
    
def mytrainingaux(X,Y,reg):
    
    reg.fit(X,Y)
                
    return reg

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred