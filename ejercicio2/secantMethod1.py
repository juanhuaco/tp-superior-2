import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

def createF(f1, f2, f3):
    return lambda p : np.array([f1(p[0], p[1], p[2]), f2(p[0], p[1], p[2]), f3(p[0], p[1], p[2])], dtype='float32')

def secantMethod3x3Iteration(F, x1, x2, x3, x4):
    F1 = F(x1)
    F2 = F(x2)
    F3 = F(x3)
    F4 = F(x4)
    #create matrix A
    A = np.array(np.zeros((4,4)))
    for j in range(4):
        A[0,j] = 1.
    for j in range(1, 4):
        A[j,0] = F1[j-1]   
    for j in range(1, 4):
        A[j,1] = F2[j-1]   
    for j in range(1, 4):
        A[j,2] = F3[j-1]   
    for j in range(1, 4):
        A[j,3] = F4[j-1]   
    #print(A)
    
    #solve Ap = b; b = [1,0,0,0]
    b = np.array([1,0,0,0], dtype='float32')
    p = np.linalg.solve(A, b)
    #print(f'p : {p}')
    return p[0]*x1 + p[1]*x2 + p[2]*x3 + p[3]*x4

def secantMethod3x3(f1, f2, f3, x1, x2, x3, x4, cantIt= 1):
    #[1 1 1 1 [F1] [F2] [F3] [F4]]p = [1,0,0,0] -> xn = pxi
    F = createF(f1, f2, f3)

    for i in range(cantIt):
        lastx = secantMethod3x3Iteration(F, x1, x2, x3, x4)
        x1 = x2
        x2 = x3
        x3 = x4
        x4 = lastx
        print(f'it nro{i+1} lastx :{x4}')

    return lastx
