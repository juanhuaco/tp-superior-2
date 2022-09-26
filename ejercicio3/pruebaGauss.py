import numpy as np
from ejercicio3.solveGauss import solve_gauss, solve_upper_triang
import sympy as sp


M = np.matrix(
    [[1.,0.5,.25],
    [1., sp.Rational(1.,3.), sp.Rational(1.,9.)],
    [1., sp.Rational(1.,4.), sp.Rational(1.,16.)]]
)

b = np.array([3.,2.,1.])

x = solve_gauss(M, b)
print(x)

#
#M = np.matrix([[1.,2.],[0.,2.]])
#b = np.array([1., 1.])
#
#x = solve_upper_triang(M, b)
#print(x)