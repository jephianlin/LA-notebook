from sage.modules.free_module_element import vector
from sage.misc.prandom import choice

def random_int_list(l, r=5):
    """
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
    return vector(random_int_list(l,r))