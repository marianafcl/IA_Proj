import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    
    min_samples_split = 2
    max_depth = 100
    regtree = tree.DecisionTreeRegressor(min_samples_split=min_samples_split, max_depth=max_depth)
    reg = mytrainingaux(X,Y, regtree)  
    return reg
    
def mytrainingaux(X,Y,reg):
    
    reg.fit(X,Y)
                
    return reg

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred