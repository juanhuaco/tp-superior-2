from tokenize import Double
import numpy as np
from sympy import *

def solve_upper_triang(A,b, presicion):
    dim=A.shape[0]
    sol=np.zeros_like(b, presicion)
    
    for i in range(dim):
        suma=b[dim-i-1]
        for j in range(i+1):
            
            suma-=A[dim-i-1,dim-j-1]*sol[dim-j-1]
    
        sol[dim-i-1]=suma/A[dim-i-1,dim-i-1]
    return sol


def solve_gauss(A,y, presicion): 
    dim=A.shape[0]

    for i in range(dim):
        aux=(1.0/A[i,i])
        for k in range(i+1,dim):
            mult=A[k,i]*aux
            A[k,:]-=A[i,:]*mult
            y[k]-=y[i]*mult


    x=solve_upper_triang(A,y, presicion)
    return x


def getResidue(A, x, b): return np.dot(A, x) - b