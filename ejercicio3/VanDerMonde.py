import numpy as  np
import sympy as smp

def getVDMMatrix(n, presicion):
    #define shape of A and x
    A = np.zeros((n, n), dtype=presicion)
    x = np.zeros(n, dtype=presicion)

    for i in range(0, n):
        x[i] = smp.Rational(1, i+2)

    for i in range(n):
        for j in range(n):
            A[i, j] = x[i]**j

    return A

def getVector(n, presicion):
    v = np.zeros(n, dtype=presicion)
    for i in range(n):
        v[i] = n-i
    return v

def getVanDerMonde(n, presicion):
    A = getVDMMatrix(n, presicion)
    b = getVector(n, presicion)
    
    return A, b