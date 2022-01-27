from copy import copy

from sage.misc.prandom import shuffle
from sage.misc.misc_c import prod

from sage.combinat.combination import Combinations

from sage.graphs.graph import Graph
from sage.graphs.digraph import DiGraph

from sage.matrix.constructor import matrix
from sage.matrix.special import zero_matrix

from sage.plot.plot import graphics_array

class list_permutation:
    def __init__(self, l):
        self.one_line = l
        self.indexing = min(l)
        self.n = len(l)
        self.base = list(range(self.indexing, self.n + self.indexing))

    def __repr__(self):
        return "%s"%self.one_line
    
    def of(self, i):
        return self.one_line[i - self.indexing]

    def digraph(self, weight=None, as_subgraph=None):
        indexing = self.indexing
        k = self.n
        V = self.base
        if weight == None:
            E = [(i, self.of(i)) for i in V]
        else:
            E = [(i, self.of(i), weight[i - indexing, self.of(i) - indexing]) for i in V]
            ### matrix weight is always 0-indexing
        g = DiGraph([V, E], loops=True)
        if as_subgraph == None:
            alpha,n = V,k
        else:
            alpha,n = as_subgraph
            g.relabel({V[i]: alpha[i] for i in range(k)}, inplace=True)
        n_pos = Graph(n).layout_circular()
        k_pos = {i: n_pos[i - indexing] for i in alpha}
        g.set_pos(k_pos)
        return g
 
    def matrix(self):
        indexing = self.indexing
        n = self.n
        P = zero_matrix(n)
        for i in self.base:
            P[i - indexing, self.of(i) - indexing] = 1
        return P

    def sign(self):
        return self.matrix().det()
    
    def weight(self, weight):
        indexing = self.indexing
        n = self.n
        V = self.base
        weights = [weight[i - indexing, self.of(i) - indexing] for i in V]
        return prod(weights, 1)

    def sort(self):
        sigmap = copy(self.one_line)
        indexing = self.indexing
        n = self.n
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

    def two_line_repr(self):
        indexing = self.indexing
        n = self.n
        r = matrix([self.base, self.one_line])
        return r

    def cycle_repr(self):
        indexing = self.indexing
        n = self.n
        base = copy(self.base)
        cycles = []
        while base != []:
            cycle = [base.pop(0)]
            while True:
                nxt = self.of(cycle[-1])
                if nxt in base:
                    base.remove(nxt)
                    cycle.append(nxt)
                else:
                    break
            cycles.append(tuple(cycle))
        return cycles
    
def random_permutation(n, indexing=1):
    nums = list(range(indexing, n + indexing))
    shuffle(nums)
    return list_permutation(nums)

def matrix_digraph(A, indexing=1, as_subgraph=None):
    k = A.dimensions()[0]
    Gamma = DiGraph(A, loops=True, multiedges=False, weighted=True)
    if as_subgraph == None:
        Gamma.relabel({i: i+indexing for i in range(k)}, inplace=True)
        alpha,n = list(range(indexing, k + indexing)), k
    else:
        alpha,n = as_subgraph
        Gamma.relabel({i: alpha[i] for i in range(k)}, inplace=True)
    n_pos = Graph(n).layout_circular()
    k_pos = {i: n_pos[i - indexing] for i in alpha}
    Gamma.set_pos(k_pos)
    return Gamma

def effective_permutations(A, indexing=1):
    ### using 0-indexing for A
    n = A.dimensions()[0]
    perms = [[]]
    for i in range(n):
        new_perms = []
        for j in range(n):
            if A[i,j] != 0:
                for perm in perms:
                    if j not in perm:
                        new_perm = copy(perm)
                        new_perm.append(j)
                        new_perms.append(new_perm)
        perms = new_perms
    return [list_permutation([i + indexing for i in perm]) for perm in perms]

def illustrate_det(A, indexing=1, each_row=4, each_size=4, to_show=True, as_subgraph=None):
    perms = effective_permutations(A, indexing)
    pics = []
    for perm in perms:
        s = perm.sign()
        w = perm.weight(A)
        H = perm.digraph(A, as_subgraph=as_subgraph)
        pic = H.plot(figsize=[each_size, each_size], 
                     edge_labels=True, 
                     title="%s * %s"%(s,w)
                    )
        pics.append(pic)
    if to_show and pics != []:
        g_array = graphics_array(pics, ncols=each_row)
        g_array.show(figsize=[g_array.ncols() * each_size, g_array.nrows() * each_size])
    return pics

def illustrate_sk(A, k, indexing=1, each_row=4, each_size=4, to_show=True):
    n = A.dimensions()[0]
    pics = []
    for alpha_m in Combinations(list(range(n)), k):
        Asub = A[alpha_m, alpha_m]
        alpha = [i + indexing for i in alpha_m]
        pics += illustrate_det(Asub, indexing, each_row, each_size, to_show=False, as_subgraph=(alpha,n))
    if to_show and pics != []:
        g_array = graphics_array(pics, ncols=each_row)
        g_array.show(figsize=[g_array.ncols() * each_size, g_array.nrows() * each_size])
    return pics