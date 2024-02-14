'''
Dictionaries
-immutable
-unordered
-key value pairs
-keys: any immutable types: int, str, tuples, NOT lists
'''

d1 = {"name" : "max", "age" : 28, "city" : "Boston", 'job' : 'js dev'}
print(d1)

'''
-use dict(noquotes)
'''

d2 = dict(name = "Mary", age = 27, city = "Boston")
value = d1['name']
print(value)



'''
-adding elements
'''
d1['email'] = 'mail.kz'
'''
-changing elements
'''
d1['email'] = 'coolmail.kz'
'''
-deleting elements (both key and value)
    -del dict[key]
    -dict.pop(key)
-deleting the last element
    -dict.popitem(key)
'''
del d1['email']


'''
-checking if an elements is in a dict
    1.if
    2.try
'''
if 'name' in d1:
    print(True)

try:
    print(d1['lastname'])
except:
    print("error")


'''
-iterating
    1.for key in dict:
    2.for key in dict.keys()
    3.for value in dict.values()
    4.both: for key, value in dict.items()
'''
for key, value in d1.items():
    print(key, value)



'''
-copying a dictioary
    1.newdict = dict(olddict)
    2.newdict = olddict.copy()
'''


'''
-merging dictionaries
    d1.update(d2)
    keys and values of d2 are transported into d1, changin the values in d1
'''

d1.update(d2)
print(d1)
