from functools import reduce

def mult(el1, el2):
    return el1 * el2

print(reduce(mult, [n for n in range(100, 1001, 2)]))