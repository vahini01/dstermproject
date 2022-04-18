import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier      
from sklearn.model_selection import cross_val_score

digits = load_digits()
clf = RandomForestClassifier(n_estimators=45000,verbose=1)
X = np.concatenate((digits.data,digits.data),axis=0)
y = np.concatenate((digits.target,digits.target)) 

clf.fit(X,y)