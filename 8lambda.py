#Lambda functions
#lambda arguments: expression
from functools import reduce

add10 = lambda x: x + 10
print(add10(5))

multiple = lambda x,y: x * y

points2d = [(1,2),(15,1),(5,-1),(10,4)]
points2d_s = sorted(points2d)


'''
sorts by the first element in a tuple
'''
print("Default sorting: ", points2d_s)

'''
-can be used to create a comparator function/specify the sorting method like in c++: sort(a.begin(), a.end(), comparator)
'''

points2d_s_y = sorted(points2d, key = lambda x: x[1], reverse = False)
print("Specified sorting: ", points2d_s_y)

points2d_s_sum = sorted(points2d, key = lambda x: x[0] + x[1])  #here x is a tuple of coordinates


"""
-can be used with the map function
-map(function, iterable)
"""

li = [1,2,3,4,5,6]    
li2 = map(lambda x: 2 * x, li)      #the same as li3 = [2 * x for x in a]
print(list(li2))

"""
-can be used with the filter function
-filter(function, iterable)     the resulting iterable will have the values from the 1st iterable for which the value of the function is true
"""

li4 = filter(lambda x: x % 2 == 0, li)      #the same as li5 = [x for x in a if x % 2 == 0]
print(list(li4))


"""
-can be used in a reduce function
-reduce(function with 2 args, iterable)
"""

li6 = reduce(lambda x,y : x * y, li)
print(li6)
