from sage.calculus.var import var

from sage.matrix.special import zero_matrix

def vtop(v):
    x = var("x")
    total = 0*x
    for i in range(len(v)):
        total += v[i] * x**i
    return total

def vtom(v, m, n):
    M = zero_matrix(v.base_ring(), m, n)
    for k in range(len(v)):
        i,j = k//n, k%n
        M[i,j] = v[k]
    return M