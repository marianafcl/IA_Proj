# Grupo 33 : Mariana -> 83520 : Carlos -> 81395

import numpy as np

def Q2pol(Q, eta=3):
    return np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]]))
	
class myRL:

    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((nS,nA))
        self.learning_rate = 0.1 
        
    def traces2Q(self, trace):
        self.Q = np.zeros((self.nS,self.nA))
        nQ = np.zeros((self.nS,self.nA))
        i = 0
        while True:            
            for tt in trace:
                #[x, a, y, r]
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + self.learning_rate * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            i += 1  
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err<1e-17:
                break 	
        return self.Q



            