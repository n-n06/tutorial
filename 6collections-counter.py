#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
a = 'aaaaaabbbbcc'
counter1 = Counter(a)
print(counter1)

'''
-Works the same as dicts
-items() to view pairs
-keys()
-values()



-most_common(n) where n is the number of elements to be outputed'''

print(counter1.most_common(2)[0])       #gives 2 most common element in a tuple
print(counter1.most_common(2)[0][1]) 
'''
-returns a list of tuples containing these elements
-can iterate by using elements()'''
print(list(counter1.elements()))
