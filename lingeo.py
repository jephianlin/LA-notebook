from sage.modules.free_module_element import vector
from sage.misc.prandom import choice
from sage.plot.colors import rainbow
from sage.plot.arrow import arrow
from sage.plot.line import line
from sage.plot.point import point

from sage.combinat.tuple import Tuples

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
                pic += vector_plot(-vec, start, viewer=viewer, color=clr)
            else:
                pic += vector_plot(vec, start, viewer=viewer, color=clr)
                pic += vector_plot(-vec, start, viewer=viewer, color=clr)
    return pic