from sage.matrix.constructor import matrix
from sage.matrix.special import zero_matrix

def sym_from_list(n, entries):
    """
    Input:
        n: integer, size of the symmetric matrix
        entries: list, entries of the symmetric matrix in row major order
    Output:
        the symmetric matrix
    """
    k = 0
    B = matrix([entries])
    A = zero_matrix(n,n).change_ring(B.base_ring())
    for i in range(n):
        for j in range(i,n):
            A[i,j] = entries[k]
            A[j,i] = entries[k]
            k += 1
    return A

def inertia(A):
    if A != A.transpose():
        raise TypeError("A must be symmetric.")
    
    eigs = A.eigenvalues()
    np,nm,nz = 0,0,0
    for eig in eigs:
        if eig > 0:
            np += 1
        if eig < 0:
            nm += 1
        if eig == 0:
            nz += 1
    return (np, nm, nz)