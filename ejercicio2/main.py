from types import ClassMethodDescriptorType
import numpy as np
import matplotlib.pyplot as plt
import ejercicio2.secantMethod1 as m1
import ejercicio2.secantMethod2 as m2
import ejercicio2.newtonMethod as n
import ejercicio2.sampleSet as sample

def ejemplo1():
    #Ejemplo 1

    print('===Ejemplo 1===')
    print('f1 = 3*x**3 - 2*y*x + 0.5*z**2 = 0')
    print('f2 = y*x**2 - 3*z*y**2 + x*z = 0')
    print('f3 = x**2 + 1.5*z**3 * y  = 0')

    f1, f2, f3, jacobian= sample.getSampleSet1()

    x = np.array([-5, 7, -7], dtype='float32')

    it=20

    #SECANT METHOD
    print('===SECANT===')
    m2.secantMethod3x3(f1,f2,f3, x, it, 0.0001)


    #NEWTON METHOD
    print('===NEWTON===')
    n.newtonMethod3x3(f1, f2, f3, jacobian, x, it)
    return

def ejemplo2():
    #Ejemplo 2

    print('===Ejemplo 2===')
    print('f1 = x**2 + y**2 +z**2 - 1 ')
    print('f2 = y**2 + z - 1')
    print('f3 = x**2 + 2*y + z**2')

    f1, f2, f3, jacobian= sample.getSampleSet2()

    x = np.array([-5, 7, -7], dtype='float32')

    it=100

    #SECANT METHOD
    print('===SECANT===')
    m2.secantMethod3x3(f1,f2,f3, x, it, 0.000001)


    #NEWTON METHOD
    print('===NEWTON===')
    n.newtonMethod3x3(f1, f2, f3, jacobian, x, it)
    
    return

def ejemplo3():
    #Ejemplo 3

    print('===Ejemplo 3===')
    print('f1(x, y, z): return x*x + z*z - 1')
    print('f2(x, y, z): return 0.5*x*x + 2*y*y + z - 1')
    print('f3(x, y, z): return -x*x -y*y + z*z - 1')
    #la aprox debe dar (0.37,-0.41,0.82) o (-0.37,-0.41,0.82)
    f1, f2, f3, jacobian= sample.getSampleSet3()

    x = np.array([-5, 7, -7], dtype='float32')

    it=1000

    #SECANT METHOD
    print('===SECANT===')
    m2.secantMethod3x3(f1,f2,f3, x, it, 0.0000001)


    #NEWTON METHOD
    print('===NEWTON===')
    n.newtonMethod3x3(f1, f2, f3, jacobian, x, it)
    
    return


def main():
    #ejemplo1()
    #ejemplo2()
    #ejemplo3()
    return

if __name__ == '__main__':
    main()