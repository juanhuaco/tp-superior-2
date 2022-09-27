from cmath import inf
import numpy as np

def getNP(A):
    N = np.zeros(A.shape)
    P = np.zeros(A.shape)
    dim = N.shape[0]
    for i in range(0, dim):
        for j in range(i, dim):
            N[i, j] = A[i,j]
        for k in range(0, i):
            P[i, k] = -A[i, k]

    return N, P 

def getLDU(A):
    dim = A.shape[0]
    L = np.zeros(A.shape)
    D = np.zeros(A.shape)
    U = np.zeros(A.shape)
    
    for i in range(dim):
        D[i,i] = A[i,i]
        for j in range(i):
            L[i, j] = A[i, j]
        for k in range(i+1,dim):
            U[i,k] = A[i,k] 
    
    return L, D, U 


def dominantArrangement(A, b):
    dim = A.shape[0]
    AA = np.zeros(A.shape)
    bb = np.zeros(dim)

    for i in range(dim):
        AA[i, :] = A[dim-1-i,:]
        bb[i]=b[dim-1-i]
    
    #pasar 1 al medio
    #mid = 0#int(dim/2)+2
    #for i in range(mid, mid+dim+1):
    #    A[:,i%dim] = AA[:,(i+1)%dim]
    #    b[i%dim] = bb[(i+1)%dim]

    
    return AA, bb



def gauss_seidel(A, y, x, it=10):
    #rearrange matrix
    A, y = dominantArrangement(A, y)
    
    ##A = N - P
    N, P = getNP(A)
    #print(f'N:{N} P:{P}')
    invN = np.linalg.inv(N)
    ##newx = Mx + c
    M = np.dot(invN, P)
    c = np.dot(invN, y)
    
    for i in range(it):
        x = np.dot(M, x) + c
        #print(f'itNro{i+1}: {x}')
    
    
    #A = L+D+U
    #L, D, U = getLDU(A)
    #invLD = np.linalg.inv(L+D)
    #G = -np.dot(invLD, U)
    #y = np.dot(invLD, y)
    #G, y = dominantArrangement(G, y)
    print(f'norm(A): {np.linalg.norm(A, inf)}')
    #print(f'M = {M} - c = {c}')
    
    #for i in range(it):
    #    x = np.dot(G, x) + y
    #    print(f'itNro{i+1}: {x}')

    return x