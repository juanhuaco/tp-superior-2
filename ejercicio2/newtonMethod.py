
import numpy as np

def getNewJacobian(jacobian, x):
    J = np.zeros((3,3), dtype='float32')
    for i in range(3):
        for j in range(3):
            f = jacobian[i,j]
            J[i,j] = f(x[0], x[1], x[2])
    return J

def newtonMethod3x3Iteration(J, f1,f2,f3, x):
    
    #J dx = -f
    f = np.array([0.,0.,0.])
    f[0] = f1(x[0], x[1], x[2])
    
    f[1] = f2(x[0], x[1], x[2])
    
    f[2] = f3(x[0], x[1], x[2])
    return np.linalg.solve(J, -f)


def newtonMethod3x3(f1, f2, f3, jacobian, x, cantIt=1):
    
    for i in range(cantIt):
        J = getNewJacobian(jacobian, x)
        x = newtonMethod3x3Iteration(J, f1, f2, f3, x) + x
        print(f'iter Nro{i+1} x: {x}')
    
    return