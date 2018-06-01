import numpy as np
from sklearn import neighbors, datasets, tree, linear_model
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

import classsol

#load input data
words = []
with open("words.txt",encoding = "ISO-8859-1")  as file:
    for line in file: 
        line = line.split(' ') #or some other preprocessing
        words.append(line) #storing everything in memory!

X = words[0]

for test in ["wordsclass.npy", "wordsclass2.npy"]:
    print("Testing " + test)
    #load output data
    Y=np.load(test)
    i = 0
    count_even_true = 0
    count_odd_true = 0
    count_even_false = 0
    count_odd_false = 0    
    
    while i < 416:
        if ((len(X[i]) % 2) == 0):
            if (Y[i] == True):
                count_even_true += 1
            else:
                count_even_false += 1
        else:   
            if (Y[i] == True):
                count_odd_true += 1
            else:
                count_odd_false += 1            
        i += 1
        
    print('Par+True:',count_even_true/416, 'Impar+True:',count_odd_true/416)
    print('Par+False:',count_even_false/416, 'Impar+False:',count_odd_false/416)