from copy import copy

from sage.misc.prandom import shuffle

from sage.graphs.digraph import DiGraph

from sage.matrix.constructor import matrix
from sage.matrix.special import zero_matrix

def random_permutation(n, indexing=1):
    nums = list(range(indexing, n + indexing))
    shuffle(nums)
    return nums

def permutation_digraph(sigma, weight=None):
    indexing = min(sigma)
    n = len(sigma)
    V = list(range(indexing, n + indexing))
    if weight == None:
        E = [(i + indexing, sigma[i]) for i in range(n)]
    else:
        E = [(i + indexing, sigma[i], weight[i, sigma[i] - indexing]) for i in range(n)]
    g = DiGraph([V, E], loops=True)
    g.set_pos(g.layout_circular())
    return g
 
def permutation_matrix(sigma):
    indexing = min(sigma)
    n = len(sigma)
    P = zero_matrix(n)
    for i in range(n):
        P[i, sigma[i] - indexing] = 1
    return P

def permutation_sign(sigma):
    return permutation_matrix(sigma).det()

def permutation_sort(sigma):
    sigmap = copy(sigma)
    indexing = min(sigma)
    n = len(sigma)
    swaps = []
    for i in range(n):
        hunt = i + indexing
        for j in range(i,n):
            if sigmap[j] == hunt:
                if i != j:
                    sigmap[j] = sigmap[i]
                    sigmap[i] = hunt
                    swaps.append((i + indexing, j + indexing))
                break
    return swaps

def two_line_repr(sigma):
    indexing = min(sigma)
    n = len(sigma)
    r = matrix([list(range(indexing, n + indexing)), sigma])
    return r

def cycle_repr(sigma):
    indexing = min(sigma)
    n = len(sigma)
    base = list(range(indexing, n + indexing))
    cycles = []
    while base != []:
        cycle = [base.pop(0)]
        while True:
            nxt = sigma[cycle[-1] - indexing]
            if nxt in base:
                base.remove(nxt)
                cycle.append(nxt)
            else:
                break
        cycles.append(tuple(cycle))
    return cycles