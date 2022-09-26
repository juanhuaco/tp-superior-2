#here comes the entiere code
import numpy as np
from VanDerMonde import getVanDerMonde
from solveGauss import solve_gauss, getResidue
import matplotlib.pyplot as plt

def vanDerMondeResidue(n):
    A, y = getVanDerMonde(n)
    sol = solve_gauss(A, y)
    r = getResidue(A, sol, y)
    r = np.linalg.norm(r, 2)
    r = np.log10(r)
    return r

def main():
    n=80
    img=np.zeros(n)
    dom=np.arange(1,n+1)
    for i in range(1, n+1):
        img[i-1] = vanDerMondeResidue(i)
    
    
    plt.title("VDM residue by n")
    plt.xlabel("n")
    plt.ylabel("residue in norm 2")
    plt.plot(dom, img)
    plt.show()

if __name__ == '__main__':
    main()
    






