from math import *
for j in range(2, 11):
    y=[0]*11
    for k in range(j):
        y[k]=exp(0.1*k)
    for k in range(j, 11):
        y[k]=3*y[k-1]-2*y[k-2]-0.1*y[k-2]
    s=""
    for k in range(j-1, 10):
        s+="("+str(k*0.1)+","+str(y[k])+")--"
    s+="(1,"+str(y[10])+")"
    print("\draw[-]"+s+";")

    
