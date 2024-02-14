'''Union and Intersections of sets'''
even = {0,2,4,6,8}
odd = {1,3,5,7,9}
primes = {2,3,5,7}

u = even.union(odd)
for i in u:
    print(i)

i = odd.intersection(primes)
print("intersection: ", i)

'''Difference and Symmetric difference of sets'''
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,2,3,11,12,13}
diff = set1.difference(set2)
print("difference", diff)

sd = set1.symmetric_difference(set2)
print("symmetric difference", sd)


'''
-Doing the same thing but without creating a new set
'''

set1.update(set2)
set1.intersection_update(set2)
set1.difference_update(set2)
set1.symmetric_difference_update(set2)
print("altered set:", set1)

'''
-issubset() and issuperset() and isdisjoint meaning no same elements
'''
set3 = {1,2,3,4,5,6}
set4 = {1,2,3}

print(set4.issubset(set3))
print(set4.issuperset(set3))
print(set4.isdisjoint(set3))


'''
-when copying through an assignment, we get the same case of the original changing in the same way as the copy
'''

oldset = {1,2,3,4,5}
newset = oldset.copy()
newset2 = set(oldset)




'''
Frozen set
-immutable set
'''

fset = frozenset([1,2,3,4,1])



