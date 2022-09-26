import numpy as np

def getSampleSet1():

    #functions
    def f1(x, y, z): return 3*x**3 - 2*y*x + 0.5*z**2
    def f2(x, y, z): return x*y*x - 3 * z * y**2 + x*z
    def f3(x, y, z): return x*x + 1.5 * z**3 * y - 0
    #jacobian
    def f1dx(x, y, z): return 9*x**2 - 2*y
    def f2dx(x, y, z): return 2*y*x  + z
    def f3dx(x, y, z): return 2*x
    def f1dy(x, y, z): return -2*x
    def f2dy(x, y, z): return x**2 - 6*z*y
    def f3dy(x, y, z): return 1.5*z**3
    def f1dz(x, y, z): return z
    def f2dz(x, y, z): return - 3 * y**2 + x
    def f3dz(x, y, z): return 4.5 * z**2 * y
    jacobian = np.matrix([[f1dx,f1dy,f1dz],[f2dx,f2dy,f2dz],[f3dx,f3dy,f3dz]])

    return f1, f2, f3, jacobian


def getSampleSet2():
    #functions
    def f1(x, y, z): return x**2 + y**2 +z**2 - 1
    def f2(x, y, z): return y**2 + z - 1
    def f3(x, y, z): return x**2 + 2*y + z**2

    #jacobian
    def f1dx(x, y, z): return 2*x
    def f2dx(x, y, z): return 0
    def f3dx(x, y, z): return 2*x
    def f1dy(x, y, z): return 2*y
    def f2dy(x, y, z): return 2*y
    def f3dy(x, y, z): return 2
    def f1dz(x, y, z): return 2*z
    def f2dz(x, y, z): return 1
    def f3dz(x, y, z): return 2*z
    jacobian = np.matrix([[f1dx,f1dy,f1dz],[f2dx,f2dy,f2dz],[f3dx,f3dy,f3dz]])

    return f1, f2, f3, jacobian

def getSampleSet3():
    def f1(x, y, z): return x*x + z*z - 1
    def f2(x, y, z): return 0.5*x*x + 2*y*y + z - 1
    def f3(x, y, z): return -x*x -y*y + z*z - 1

    def f1dx(x, y, z): return 2*x
    def f1dy(x, y, z): return 0
    def f1dz(x, y, z): return 2*z
    def f2dx(x, y, z): return x
    def f2dy(x, y, z): return 4*y
    def f2dz(x, y, z): return 1
    def f3dx(x, y, z): return -2*x
    def f3dy(x, y, z): return -2*y
    def f3dz(x, y, z): return 2*z
    jacobian = np.matrix([[f1dx,f1dy,f1dz],[f2dx,f2dy,f2dz],[f3dx,f3dy,f3dz]])

    return f1, f2, f3, jacobian

