# DZ 19
from math import inf # из(from) match импорт inf (Positive infinity)

def divide(first, second):
    if second == 0:
        return inf
    res = first / second
    return res