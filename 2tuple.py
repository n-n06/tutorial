'''
Tuple
-Ordered
-Immutable/not changing
-Allows duplicate elements
'''
import sys
import timeit


t1 = ("max", 28, "min")
t2 = 1, 'max', 'min'

'''
-a one element tuple must have a comma, otherwise it will not be a tuple'''
t3 = ('a',)   #is a tuple
t3 = ('a')  #is a string

'''
-create a tuple using tuple(iterable)
'''

t5 = tuple(['max',2,'min'])

'''
-the same indexes as in lists. also negative
-iterable
-the same in method
-the same len method

-.count(item) method
'''

t6 = ('a', 'p', 'p')
print(t6.count('p'))

'''
-.index(item)   the index of the first occurence of the element
'''
print(t6.index('p'))

'''
-convertible to a list and vice versa
'''

'''
-slicing the same as lists
'''

'''
-UNPACKING
    -number of elements must match the tuples' length
    -to avoid an error - use *
'''

t7 = "Max", 28, "Boston"
name, age, city = t7
print(name)
print(age)
print(city)

t8 = (1,2,3,4,5,6)
i1, *i_mid, i_last = t8     #all the elements from the middle are stored in i_mid as a list
print(i_mid)


'''
-Tuples are faster than lists sometimes
'''
print(timeit.timeit(stmt='(0,1,2,3,4,5)', number = 1000000))

