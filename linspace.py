from sage.misc.prandom import choice

from sage.calculus.var import var
from sage.calculus.all import symbolic_expression

from sage.symbolic.ring import SR

from sage.modules.free_module_element import vector
from sage.matrix.special import zero_matrix
from sage.matrix.special import diagonal_matrix

from lingeo import column_space_matrix

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

def ptov(p, d):
    p_poly = symbolic_expression(p).polynomial(SR)
    v = vector([p_poly[i] for i in range(d+1)])
    return v

def mtov(A):
    return vector(A.list())

def projection_on_vector(u, v, return_mtx=False):
    """return the projection of u onto v"""
    v_len2 = v.inner_product(v)
    p = (u.inner_product(v) / v_len2) * v
    if return_mtx:
        v_mtx = matrix(v)
        P = v_mtx.conjugate_transpose() * v_mtx / v_len2
        return p, P
    else:
        return p
    
def projection_on_colspace(u, A, return_mtx=False):
    """return the projection of u onto Col(A)"""
    B = column_space_matrix(A)
    BTBinv = (B.transpose() * B).inverse()
    P = B * BTBinv * B.transpose()
    p = P * u
    if return_mtx:
        return p, P
    else:
        return p
    
def QR(A):
    """
    Input: 
        A: m x n matrix over SR of rank r
    Output:
        Q: m x r column orthonormal matrix 
        R: r x n upper triangular matrix
    """
    m,n = A.dimensions()
    if A.is_zero():
        return None, zero_matrix(m,n)
    for j in range(n):
        if not A[:,j].is_zero():
            first_j = j
            break

    Q = A[:,first_j]
    Q = Q.change_ring(SR)
    R = zero_matrix(SR, m, n) ### remove extra rows in the end
    R[first_j,0] = 1
    
    for j in range(first_j, n):
        u = A[:,j]
        QTQinv = diagonal_matrix( 1/q.inner_product(q) for q in Q.transpose() )
        coefs = QTQinv * Q.conjugate_transpose() * u
        uhat = u - Q * coefs
        R[:coefs.dimensions()[0],j] = coefs
        if not uhat.is_zero():
            Q = Q.augment(uhat)
            R[coefs.dimensions()[0], j] = 1
    R = R[:Q.dimensions()[1], :]
    return Q, R

### classes of vector spaces
class Rn:
    def __init__(self, n):
        self.dim = n
    def __repr__(self):
        return "The vector space of all vectors over RR of length %s."%self.dim
    
class poly:
    def __init__(self, d, zeros=None):
        self.deg = d
        self.zeros = zeros
        self.num_zeros = 0 if zeros == None else len(zeros)
        self.dim = max(0, d + 1 - self.num_zeros)
    def __repr__(self):
        if self.deg == -1:
            return "The vector space consisting of only the zero polynomial."
        if self.zeros == None:
            return "The vector space of all polynomials p of degree at most %s."%self.deg
        else:
            return "The vector space of all polynomials p of degree at most %s "%self.deg + \
        "such that p(x) = 0 for all x in %s."%self.zeros
    
class mtx:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.dim = m * n
    def __repr__(self):
        return "The vector space of all %s x %s matrices."%(self.m, self.n)
    
class sym_mtx:
    def __init__(self, n):
        self.n = n
        self.dim = n * (n + 1) / 2
    def __repr__(self):
        return "The vector space of all %s x %s symmetric matrices."%(self.n, self.n)
    
class skew_mtx:
    def __init__(self, n):
        self.n = n
        self.dim = n * (n - 1) / 2
    def __repr__(self):
        return "The vector space of all %s x %s skew-symmetric matrices."%(self.n, self.n)

def nvspace(n, poly_zeros=3):
    want = [Rn(n), poly(n-1)]
    for i in range(1, poly_zeros + 1):
        want.append(poly(n-1 + i, list(range(1, i+1))))
    for i in range(1,n+1):
        if n % i == 0:
            want.append(mtx(i, n // i))
        if sym_mtx(i).dim == n:
            want.append(sym_mtx(i))
        if skew_mtx(i).dim == n:
            want.append(skew_mtx(i))
    return want

def random_nvspace(n, poly_zeros=3):
    return choice(nvspace(n, poly_zeros))