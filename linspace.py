from sage.calculus.var import var

from sage.symbolic.ring import SR

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