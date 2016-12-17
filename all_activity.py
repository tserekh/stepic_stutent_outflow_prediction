# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:31:29 2016

@author: Artem 
"""
import csv
from random import randint
from fun3 import get_X
from fun3 import dic_to_list
from fun3 import get_targed
from fun3 import cbind
from fun3 import make_3d
from sklearn.metrics import f1_score
from sklearn.ensemble import GradientBoostingClassifier

#border=90
filename="C:/Users/Artem/Documents/stepic/kaggle/user_activity.csv"
X_train=[]
for el in make_3d():
    print(el)
    if len(X_train)==0:
        X_train=get_X(filename,el[0],el[1])
    else:
        X_train=cbind( X_train,  get_X(filename, el[0], el[1])  )

filename="C:/Users/Artem/Documents/stepic/kaggle/user_activity_test.csv"
X_test=[]
for el in make_3d():
    print(el)
    if len(X_test)==0:
        X_test=get_X(filename,el[0],el[1])
    else:
        X_test=cbind( X_test,  get_X(filename, el[0], el[1])  )   
mdepth = 3
Nest=100
Nmax=16620
index1=[]
index2=[]
index3=[]
#for i in range(Nmax):
for i in range(Nmax):
    radn_n = randint(0,2)
    if radn_n==0:
        index1.append(i)
    elif radn_n==1:
        index2.append(i)
    elif radn_n==2:
        index3.append(i)                 
#print(index2)
'''
N1=5000
N2=10000
N3=15000
index1=list(range(N1))
index1=list(range(N1,N2))
index1=list(range(N2,N3))
'''
X1=[X_train[i] for i in index1]
X2=[X_train[i] for i in index2]
X3=[X_train[i] for i in index3]

Y_train=get_targed("C:/Users/Artem/Documents/stepic/kaggle/targets.csv")

Y1=[Y_train[i] for i in index1]
Y2=[Y_train[i] for i in index2]
Y3=[Y_train[i] for i in index3]

clf1 = GradientBoostingClassifier(n_estimators =Nest,max_depth = mdepth)
clf1.fit(X1, Y1)
pY2=clf1.predict(X2)
#print(mean_squared_error(Y2,pY2))
print(f1_score(Y2,pY2))
p1Y_test=clf1.predict_proba(X_test)

clf2 = GradientBoostingClassifier(n_estimators= Nest,max_depth = mdepth)
clf2.fit(X2, Y2)
pY3=clf2.predict(X3)
#print(mean_squared_error(Y3,pY3))
print(f1_score(Y3,pY3))
p2Y_test=clf2.predict_proba(X_test)

clf3 = GradientBoostingClassifier(n_estimators =Nest,max_depth = mdepth)
clf3.fit(X3, Y3)
pY1=clf3.predict(X1)
#print(mean_squared_error(Y1,pY1))
print(f1_score(Y1,pY1))
p3Y_test=clf3.predict_proba(X_test)

prY_test=[]
for i in range(len(p3Y_test)):
    a=[   (p1Y_test[i][1]+p2Y_test[i][1]+p3Y_test[i][1])/3   ]
    prY_test.append(a)

with open('C:/Users/Artem/Documents/stepic/submit_SCORE time and ID + .csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')  
    a.writerows(prY_test)  
