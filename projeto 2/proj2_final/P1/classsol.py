# Grupo 33 : Mariana -> 83520 : Carlos -> 81395
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib

from sklearn.model_selection import cross_val_score

def hasA(string):
    for char in string:
        if char in 'a':
            return 1
    return 0

def features(X):
    
    F = np.zeros((len(X),2))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = hasA(X[x])

    return F     

def mytraining(f,Y):
    n_neighbors = 5
    weights = 'distance'
    metric= 'manhattan' # Distance Function: sum(|x - y|)
    
    clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, metric=metric)
    clf.fit(f, Y) # fit the data into the classifier
    
    '''
    min_samples_split = 3
    max_depth = 5
    clf = tree.DecisionTreeClassifier(min_samples_split=min_samples_split,max_depth=max_depth)
    clf.fit(f, Y)
    '''
    
    return clf
    

def myprediction(f, clf):
    Ypred = clf.predict(f) 

    return Ypred




