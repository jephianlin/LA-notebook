from copy import copy

from sage.misc.prandom import shuffle
from sage.misc.misc_c import prod

from sage.graphs.digraph import DiGraph

from sage.matrix.constructor import matrix
from sage.matrix.special import zero_matrix

def random_permutation(n, indexing=1):
    nums = list(range(indexing, n + indexing))
    shuffle(nums)
    return list_permutation(nums)

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

    def digraph(self, weight=None):
        indexing = self.indexing
        n = self.n
        V = self.base
        if weight == None:
            E = [(i, self.of(i)) for i in V]
        else:
            E = [(i, self.of(i), weight[i - indexing, self.of(i) - indexing]) for i in V]
            ### matrix weight is always 0-indexing
        g = DiGraph([V, E], loops=True)
        g.set_pos(g.layout_circular())
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