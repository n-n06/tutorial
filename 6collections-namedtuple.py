from collections import namedtuple

point = namedtuple('point', 'x,y,z')
pt = point(1,4,7)
print(pt)

'''
-Printing out key names as a tuple(namedtuple does not have a keys attr)
'''
print(point._fields)


'''
-Accessing elements
    1.by parameter-/keyname
    2.by index
    3.getattr
'''
print(pt.x)
print(pt[2])
print(getattr(pt, 'y'))



'''
-_make() turns an iterable into a namedtuple

'''
li = [5, 16, 3]
namedli = point._make(li)
print('a list as a namedtuple ', namedli)


'''
-_asdict() returns a dict representation of a named tuple

'''
pt_dict = pt._asdict()
print("a namedtuple as a dict ", pt._asdict(), end='\n')
print(pt_dict)


'''
-** turns a dict into a namedtuple
'''
dict = {'x' : 6, 'y' : 2, 'z' : 5}
nameddict = point(**dict)
print("a dict as a namedtuple ", nameddict)


'''
- _replace() changes value of keys
'''

print(pt._replace(x = 3))


'''
- __new__ creating and returning a new object of class point
'''
print([point.__new__(point, 15, 31, 0)])


'''
- __getnewargs__ printing out the values as a plain tuple
'''
print(pt.__getnewargs__())
