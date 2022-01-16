from copy import copy

from sage.misc.prandom import choice
from sage.plot.colors import rainbow
from sage.plot.arrow import arrow
from sage.plot.line import line
from sage.plot.point import point

from sage.combinat.combination import Combinations
from sage.combinat.tuple import Tuples

from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.rings.qqbar import QQbar
from sage.symbolic.ring import SR

from sage.modules.free_module_element import vector
from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.matrix.special import zero_matrix
from sage.matrix.special import elementary_matrix

# from sage.plot.text import text
# from sage.plot.plot3d.shapes2 import text3d

# def tt(txt, pt, **kwds):
#     if len(pt) == 2:
#         return text(txt, pt, **kwds)
#     if len(pt) == 3:
#         return text3d(txt, pt, **kwds)
#     else:
#         raise InputError("pt can only be in R2 or R3")

def random_int_list(l, r=5):
    """
    return a random integer list of length l with entries bounded by +- r
    
    Input:
        l: integer; length of the list
        r: integer; entries are between -r to r inclusive
    Output:
        a (nonzero) list whose elements are random"""
    nums = list(range(-r,r+1))
    while True:
        out = []
        for _ in range(l):
            out.append(choice(nums))
        if out != [0]*l:
            break
    return out

def random_int_vec(l, r=5):
    """
    return a random integer list of length l with entries bounded by +- r
    """
    return vector(random_int_list(l,r))

def draw_two_vec(x, y):
    yx = y.inner_product(x) / x.norm()**2
    yy = (y - yx*x).norm()
    return arrow((0,0), (x.norm(), 0), color="red") + arrow((0,0), (yx, yy), color="blue")

def vector_plot(v=None, start=None, dim=None, viewer='threejs', **kwds):
    if dim == None:
        dim = len(v)
    if dim == 2:
        if v == None:
            v = vector([0,0])
        if start == None:
            start = vector([0,0])
        pic = arrow(start, start+v, **kwds)
    if dim == 3:
        if v == None:
            v = vector([0,0,0])
        if start == None:
            start = vector([0,0,0])
        pic = arrow(start, start+v, viewer=viewer, **kwds)
    return pic

def draw_span(vectors, p=None, dim=None, viewer='threejs', width=5):
    """
    draw a span  
    
    Input:
        vectors: a list of vectors
        p: vector for shifting the space
        dim: dimension can be 2 or 3
            usually no need to set up
        viewer: one of 'threejs', 'jmol', or 'tachyon'
        width: the coefs for span has abs value at most width
        
    Output:
        a drawing of the span
    """
    if dim == None:
        dim = len(vectors[0])
    origin = vector([0]*dim)
    pic = point(origin, size=100, color="orange")
    if p == None:
        p = vector([0]*dim)
    else: 
        pic += vector_plot(p, color="orange")
    
    num_vec = len(vectors)
    clrs = rainbow(num_vec)
    all_coefs = [coef for coef in Tuples(range(-width,width+1), num_vec) if sum(map(abs,coef)) < width]
#     pic += vector_plot(dim=dim, viewer=viewer)
    for coefs in all_coefs:
        start = p + sum(coefs[i]*vectors[i] for i in range(num_vec))
        for i in range(num_vec):
            vec = vectors[i]
            clr = clrs[i]
            if coefs[i] > 0:
                pic += vector_plot(vec, start, viewer=viewer, color=clr)
            elif coefs[i] < 0:
                pic += vector_plot(vec, start - vec, viewer=viewer, color=clr)
            else:
                pic += vector_plot(vec, start, viewer=viewer, color=clr)
                pic += vector_plot(vec, start - vec, viewer=viewer, color=clr)
    return pic

def random_ref(m, n, r, bound=5, return_pivots=False):
    """A generator of 
    random reduced echelon form 
    (where the pivots are 1)
    
    Input:
        m, n: integers
        r: positive integer with r <= m and r <= n
        bound: positive integer
            |matrix entries| <= bound
        return_pivots: boolean
            if True, return the pivots also
    Output:
        an m x n matrix with rank r
        in its reduced echelon form
        whose pivots are 1.
        Note: the first pivot always locates at (0,0).
    """
    R = zero_matrix(m,n)
    if r == 0:
        return R, [] if return_pivots else R
    all_numbers = list(range(-bound, bound+1))
    all_choices = list(Combinations(list(range(1,n)),r-1))
    pivots = [0] + choice(all_choices)
    pivots += [n]
    for i in range(r):
        j = pivots[i]
        R[i,j] = 1
        for ii in range(i+1):
            for jj in range(j+1, pivots[i+1]):
                R[ii,jj] = choice(all_numbers)
    R = R.change_ring(QQ)
    pivots.remove(n)
    if return_pivots:
        return R, pivots
    else:
        return R

def random_good_matrix(m, n, r, bound=5, return_answer=False):
    """A generator of 
    matrix whose Gaussian elimination is easy.
    
    Input:
        m, n: integers
        r: positive integer with r <= m and r <= n
        bound: positive integer
            |coeff for row operation| <= bound
        return_answer: boolean
            if True, return the reduced echelon form and the pivots also.
    Output:
        an m x n matrix with rank r
        whose Gaussian elimination is easy.
    """
    R, pivots = random_ref(m, n, r, return_pivots=True)
    A = copy(R)
    pivots_rev = copy(pivots)
    pivots_rev.reverse()
    all_numbers = list(range(-bound, bound+1))
    ### upward mix 
    for i in range(r):
        j = pivots_rev[i]
        for ii in range(i):
            A[ii,:] += A[i,:] * choice(all_numbers)
    ### downward mix
    for i in range(r):
        j =  pivots_rev[i]
        for ii in range(i+1,m):
            A[ii,:] += A[i,:] * choice(all_numbers)
    if return_answer:
        return A, R, pivots
    else:
        return A
    
def row_operation_process(A, inv=False):
    """
    Input:
        A: mxn matrix over ZZ, QQ, or QQbar
        rev: whether to return [E1^{-1}, ..., Ek^{-1}] instead
             such that A = E1^{-1}...Ek^{-1}R
    Output:
        Let R be the reduced echelon form of A.
        Return a list [E1, ..., Ek] such that Ek...E1A = R.
    """
    R = copy(A)
    if R.base_ring() in [ZZ, QQ]:
        R.change_ring(QQ)
        field = QQ
    if R.base_ring() in [QQbar, SR]:
        try:
            R.change_ring(QQbar)
            field = QQbar
        except NotImplementedError:
            raise TypeError("Input matrix should be over at least QQbar")
            
    i,j = 0,0
    m,n = R.dimensions()
    elems = []
    for j in range(n):
        for k in range(i,m):
            if R[k,j] != 0:
                if k != i:
                    R.swap_rows(i,k)
                    elems.append(elementary_matrix(field, m, row1=i, row2=k))
                if R[i,j] != 1:
                    k = R[i,j]
                    R.rescale_row(i, 1/k)
                    elems.append(elementary_matrix(field, m, row1=i, scale=1/k))
                for h in range(m):
                    if h != i and R[h,j] != 0:
                        k = R[h,j]
                        R.add_multiple_of_row(h, i, -k)
                        elems.append(elementary_matrix(field, m, row1=h, row2=i, scale=-k))
                i += 1
                break
    elems_inv = []
    for E in elems:
        elems_inv.append(E.inverse())
    if inv:
        return elems_inv
    else:
        return elems

def find_pivots(ref):
    """Find the pivots of a reduced echelon form.
    
    Input:
        ref: a matrix in reduced echelon form
    Outpu: 
        a list of of indices of the pivots
    """
    m,n = ref.dimensions()
    pivots = []
    for i in range(m):
        for j in range(n):
            if ref[i,j] != 0:
                pivots.append(j)
                break
        else:
            break    
    return pivots

def betak_solver(ref, free, k):
    """Return the solution for 
    ref * x = 0
    whereas the k-th (1-indexing) free variable is 1
    while all other free variables are 0.
    
    Input:
        ref: matrix in reduced echelon form
        free: a list of indices of the free variables
        k: positive integer
    Output:
        A column vector beta_k (n x 1 matrix)
        that satisfies ref * beta_k = 0
        whereas the k-th (1-indexing) free variable is 1
        while all other free variables are 0.
    """
    m,n = ref.dimensions()
    pivots = [j for j in range(n) if j not in free]
    rank = len(pivots)
    betak = [0] * n
    ### k is 1-indexing
    ### free is 0-indexing
    betak[free[k-1]] = 1
    for i in range(rank-1,-1,-1):
        j = pivots[i]
        betak[j] = -sum([ref[i,jj]*betak[jj] for jj in range(j+1,n)])
    return  matrix(n,betak)

def row_space_matrix(A):
    m,n = A.dimensions()
    R = A.rref()
    pivots = find_pivots(R)
    free = [i for i in range(n) if i not in pivots]
    r = len(pivots)
    Rp = R[:r,:] ### r x n
    H = zero_matrix(Rp.base_ring(), n, n-r) ### n x (n-r)
    H[pivots] = -Rp[:, free]
    H[free] = identity_matrix(n-r)
    return Rp

def kernel_matrix(A):
    m,n = A.dimensions()
    R = A.rref()
    pivots = find_pivots(R)
    free = [i for i in range(n) if i not in pivots]
    r = len(pivots)
    Rp = R[:r,:] ### r x n
    H = zero_matrix(Rp.base_ring(), n, n-r) ### n x (n-r)
    H[pivots] = -Rp[:, free]
    H[free] = identity_matrix(n-r)
    return H

def column_space_matrix(A):
    m,n = A.dimensions()
    AI = A.augment(identity_matrix(m), subdivide=True)
    RB = AI.rref()
    R = RB[:,:n]
    B = RB[:,n:]
    pivots = find_pivots(R)
    free = [i for i in range(n) if i not in pivots]
    r = len(pivots)
    C = A[:, pivots] ### m x r
    Bp = B[r:,:] ### (m-r) x m
    return C

def left_kernel_matrix(A):
    m,n = A.dimensions()
    AI = A.augment(identity_matrix(m), subdivide=True)
    RB = AI.rref()
    R = RB[:,:n]
    B = RB[:,n:]
    pivots = find_pivots(R)
    free = [i for i in range(n) if i not in pivots]
    r = len(pivots)
    C = A[:, pivots] ### m x r
    Bp = B[r:,:] ### (m-r) x m
    return Bp