
import numpy as np

def getNewJacobian(J, f1, f2, f3, x, d):

    J[0, 0] = ( f1(x[0] + d, x[1]    , x[2]    ) - f1(x[0],x[1],x[2]) ) / d
    J[0, 1] = ( f1(x[0]    , x[1] + d, x[2]    ) - f1(x[0],x[1],x[2]) ) / d
    J[0, 2] = ( f1(x[0]    , x[1]    , x[2] + d) - f1(x[0],x[1],x[2]) ) / d
    J[1, 0] = ( f2(x[0] + d, x[1]    , x[2]    ) - f2(x[0],x[1],x[2]) ) / d
    J[1, 1] = ( f2(x[0]    , x[1] + d, x[2]    ) - f2(x[0],x[1],x[2]) ) / d
    J[1, 2] = ( f2(x[0]    , x[1]    , x[2] + d) - f2(x[0],x[1],x[2]) ) / d
    J[2, 0] = ( f3(x[0] + d, x[1]    , x[2]    ) - f3(x[0],x[1],x[2]) ) / d
    J[2, 1] = ( f3(x[0]    , x[1] + d, x[2]    ) - f3(x[0],x[1],x[2]) ) / d
    J[2, 2] = ( f3(x[0]    , x[1]    , x[2] + d) - f3(x[0],x[1],x[2]) ) / d
    return J

def secantMethod3x3Iteration(J, f1,f2,f3, x):
    
    #J dx = -f
    f = np.array([0.,0.,0.])
    f[0] = f1(x[0], x[1], x[2])
    f[1] = f2(x[0], x[1], x[2])
    f[2] = f3(x[0], x[1], x[2])
    
    return np.linalg.solve(J, -f)


def secantMethod3x3(f1, f2, f3, x, cantIt=1, d=0.00000001):
    J = np.zeros((3,3), dtype='float32')

    for i in range(cantIt):
        J = getNewJacobian(J, f1, f2, f3, x, d)
        x += secantMethod3x3Iteration(J, f1, f2, f3, x)
        print(f'iter Nro{i+1} x: {x}')
    
    return