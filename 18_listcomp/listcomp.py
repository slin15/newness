'''
Susan Lin
SoftDev2 pd 08
K #18: Getting Clever with List Comprehensions
T 2019-04-16
'''

'''
1. Write a list comprehension to generate a list of all Pythagorean triples on range [0,n).
'''
def pythagorean(n):
    return [(a,b,c) for a in range(n+1) for b in range(a) for c in range(b) if a*a == b*b + c*c]

#print(pythagorean(25))

'''
2. Implement quicksort in the most succinct way possible using list comprehension(s).
'''
def quicksort(list):
    if len(list) < 2:
        return list
    partition = list[0]

'''
union of the sets a and b, denoted a u b
'''
def union(a, b):
    return a[:]+[x for x in b if x not in a]

print(union([1,2,3], [2,3,4]))

'''
intersection of sets a and b, denoted a n b
'''
def intersection(a, b):
    return [x for x in a if x in b]

print(intersection([1, 2, 3], [2, 3, 4]))

'''
difference of the sets u and a, denoted u/a
'''
def difference(u, a):
    return [x for x in u if x not in a]

print(difference([1, 2, 3], [2, 3, 4]))
print(difference([2, 3, 4], [1, 2, 3]))

'''
symmetric difference of a and b, denoted a triangle b
'''
def sym_diff(a, b):
    return difference(union(a, b), intersection(a, b))

print(sym_diff([1,2,3], [2,3,4]))

'''
cartesian product of a and b, denoted a x b
all ordered possible pairs of a and b
'''
def cart(a, b):
    return [(x,y) for x in a for y in b]

print(cart([1,2,3], [2,3,4]))

'''
??? of sets a and b, denoted a y b 
'''
