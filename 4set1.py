'''
Sets
-mutable
-unordered
-No duplicates
'''

s1 = {1,2,3,4}
s2 = {1,2,3,4,1,2,3}
print(s2)

'''
-using set() function with a list
'''

s3 = set([1,2,3,4,5])
print(s3)

'''
-using set() with a string produces a set of chars in an arbitrary order with no dupliactes
'''

s4 = set("Hello world")
print("seted string: ", s4)

'''
-to create an empty set use set() rather than {}
'''

'''
-adding and removing elements
'''
s1.add(5)
s1.remove(3)
'''
-removing objects without getting an error message when the element is not found in the set: discard()
'''
s1.discard(6)
print(s1)

'''
-use clear() to delete everything and pop() to delete and return some random element

-the same iteration and condition syntaxes
'''


