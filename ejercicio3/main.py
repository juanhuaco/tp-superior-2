#here comes the entiere code
import numpy as np
from VanDerMonde import getVanDerMonde
from solveGauss import solve_gauss, getResidue
import matplotlib.pyplot as plt

def vanDerMondeResidue(n, presicion):
    A, y = getVanDerMonde(n, presicion)
    sol = solve_gauss(A, y, presicion)
    r = getResidue(A, sol, y)
    r = np.linalg.norm(r, 2)
    #r = np.log10(r)
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

def main():
    n=80
    graphResidue(n, "float64")
    graphResidue(n, "float32")

if __name__ == '__main__':
    main()
    






