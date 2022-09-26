import numpy as np
from sympy import *
def solve_upper_triang(A,b):
    #[[1, 2],[0, 2]] ; [1, 1 ] x=0, y=1/2
    
    dim=A.shape[0] #->2

    sol=np.zeros_like(b) #->[0, 0]

    for i in range(dim): # i->0
        suma=b[dim-i-1] #->last element - sum = 1
        for j in range(i+1): #j=0
            suma=suma - A[dim-i-1,dim-j-1]*sol[dim-j-1]#->A[1,1]*0
            sol[dim-i-1]=suma/A[dim-i-1,dim-i-1]#sol[1]=0/A[1,1]
            #print(f'i: {i} - j: {j} - suma: {suma} - sol{sol}')
    
    return sol



def solve_gauss(A,y): 
    dim=A.shape[0]

    for i in range(dim):
        aux=(1.0/A[i,i])
        for k in range(i+1,dim):
            mult=A[k,i]*aux
            A[k,:]-=A[i,:]*mult
            y[k]-=y[i]*mult


    x=solve_upper_triang(A,y)
    return x