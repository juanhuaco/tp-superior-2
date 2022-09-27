#here comes the entiere code
import numpy as np
from VanDerMonde import getVanDerMonde
from solveGauss import solve_gauss, getResidue
import matplotlib.pyplot as plt
from gaussSeidel import gauss_seidel, dominantArrangement
import time as t

def vanDerMondeResidue(n, presicion):
    A, y = getVanDerMonde(n, presicion)
    sol = solve_gauss(A, y, presicion)
    r = getResidue(A, sol, y)
    r = np.linalg.norm(r, 2)
    r = np.log10(r)
    return r

def graphResidue(n, presicion):
    img=np.zeros(n)
    dom=np.arange(1,n+1)
    for i in range(1, n+1):
        img[i-1] = vanDerMondeResidue(i, presicion)
    
    plt.title("VDM residue by n")
    plt.xlabel("n")
    plt.ylabel(f'residue in norm 2 (log10) in {presicion}')
    plt.plot(dom, img)
    plt.show()

def ejercicio3by3c():
    n=80
    print("===EJERCICIO 3.b y 3.c===")
    graphResidue(n, "float64")
    graphResidue(n, "float32")
    return

def ejercicio3d():
    print('===EJERCICIO 3.d===')
    A, y = getVanDerMonde(20, "float64")
    x = gauss_seidel(A, y, y, 1000)
    print(x)
    return

def ejercicio3e():
    n=200
    img = []
    dom = np.arange(1, n+1)
    start = t.time()
    for i in range(1, n+1):
        start = t.time()
        A, y = getVanDerMonde(i,'float64')
        gauss_seidel(A, y, y, 1000)
        end= t.time()
        img.append(end-start)
    
    plt.plot(dom, img)
    plt.xlabel("n")
    plt.ylabel("time")
    plt.title("gaussSeidel time spent by n")
    plt.show()

    return

def main():
    #ejercicio3by3c()
    #ejercicio3d()
    ejercicio3e()
    

if __name__ == '__main__':
    main()
    






