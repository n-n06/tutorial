"""#Exceptions"""
# x = -1
# if (x < 0):
#     raise Exception("x should be pos")

#another way of throwing an exc is to write an assertion that will cause a exc if false
# assert(x>0), 'x is negative'

"""
-can use try except in order for a program not to stop if an error/exception occurs
"""

try:
    a = 6 /0
except:
    print("+Infinity")

#to view the name of the exception

# try:
#     b = 4 / 0
# except Exception as exp:
#     print(exp)

#possible to use the name of the exceptions(the one displayed in the terminal)

"""
-use else for the case with no exceptions
"""

try:
    b = 5 / 1
except ZeroDivisionError as error:
    print(error)
else:
    print("yehehe")
finally:
    print("it all returns to nothing")

"""
-use finally clause that will be printed no matter what(both when exceptions or else commands are activated)
"""



"""
-deifining a new class of exceptions
"""


class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value


class ValueTooHighError(Exception):
    pass


def checkvalue(x):
    if x > 100:
        raise ValueTooHighError("ur gey")
    if x < 5:
        raise ValueTooSmallError("no gay: ", x)

try:
    checkvalue(200)
except ValueTooHighError as v:
    print("Simple class exception ", v)


#can be used to print out all of the data that caused the error by storing it as attributes in a class
try:
    checkvalue(1)
except ValueTooSmallError as v:
    print("Complicated class exception ", v.message, v.value)