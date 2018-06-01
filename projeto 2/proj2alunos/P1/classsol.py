import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def features(X):
    
    F = np.zeros((len(X),2))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = hasA(X[x])
        #F[x,3] = accent(X[x])
        #F[x,4] = alpha(X[x])
    
        
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
    

def odd(string):
    if(len(string)%2 == 0):
        return 0
    return 1
    
def mytrainingaux(f,Y,par):
    
    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)

    return Ypred

def countV(x):
    v = "aeiouáàãâéèêíìîóòõôúùû"
    count = 0
    for c in x:
        if c in v:
            count += 1
    return count

def accent(x):
    v = "áàãâéèêíìîóòõôúùû"
    for c in x:
        if c in v:
            return 1
    return 0

def alpha(x):
    return ord(x[0]) - ord('a')

def checkO(x):
    if x[-1] == 'a':
        return 1
    elif x[-1] == 'o':
        return 0
    return 2

def hasA(string):
    for char in string:
        if char in 'a':
            return 0
    return 1