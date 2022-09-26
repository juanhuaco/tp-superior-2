import numpy as  np
import sympy as smp

def getVDMMatrix(n):
    #define shape of A and x
    A = np.zeros((n, n))
    x = np.zeros(n)

    for i in range(0, n):
        x[i] = smp.Rational(1, i+2)

    for i in range(n):
        for j in range(n):
            A[i, j] = x[i]**j

    return A

def getVector(n):
    v = np.zeros(n)
    for i in range(n):
        v[i] = n-i
    return v

def getVanDerMonde(n):
    A = getVDMMatrix(n)
    b = getVector(n)
    
    return A, b