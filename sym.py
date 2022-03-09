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