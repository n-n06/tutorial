import itertools
import collections
import operator

#itertools basically implements functions from discrete math, namely from set theory and combinatorics
#itertools: product(cartesian), permutations, combinations, combinations with replacement, accumulate, groupby, infinite iterators
a = [1,2]
b = [3]
prod = itertools.product(a,b, repeat=2)
print(f"cartesian product of {a} and {b}", tuple(prod))


d = [1,2,3]
perm = itertools.permutations(d)
print(f"permutations of {d} ", tuple(perm))
perm2 = itertools.permutations(d, 2)
print(f"restricted permutations: ", tuple(perm2))


e = [1,2,3,4]
comb = itertools.combinations(e, 2)
print(f"C 4 to 2 over {e}: ", tuple(comb))
comb_wr = itertools.combinations_with_replacement(e,2)
print("C 4 to 2 with repetitions: ", tuple(comb_wr))


g = [1,2,6,5,3,4]
g_acc = itertools.accumulate(g, func = max)
print(f"an accumulated {g}: ", tuple(g_acc))



def smaller_than_3(x):
    return x < 3
h = [1,2,3,4]
#group = itertools.groupby(h, key = smaller_than_3) we can do better
group = itertools.groupby(h, key = lambda x: x < 3)
for key, value in group:
    print(key, tuple(value))


'''
-INFINITE ITERATORS
1. count
for i in count(10):
    print(i)
    if (i == 15): break
basically counting from 10 to inf while we do not reach some kind of a stop statement
2. cycle
for i in cycle(list):
    print(i)
basically infinitely printing out the elements of an iterable
3. repeat
for i in repeat(1):
    print(i) 
basically printing out 1s infinitely
    print(i, b) we stop printing out at b
'''