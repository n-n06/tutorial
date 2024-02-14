"""
-Converting from strings to lists using split with default argument of blank(" ")"""
string1 = "adf asdf asdf asdf"
list1 = string1.split()
print(list1)

'''
-Converting from lists to string'''
string2 = ''.join(list1)
print(string2)




#String operations using %s for strings
var = 4
var2 = 3.14152
string_m = "low"
string3 = "the value is %s" % string_m
print(string3)
'''
    -%d for integers
'''
string3 = "the value is %d" % var
print(string3)
'''
    -%f for floats (6 digits after the dec point)
    -%.nf where n is an integer number representing the number of digits after a decimal point
'''
string3 = "pi is appr %f" %var2 
print(string3)




#String operations using format()
string = 'pi is appr {}'.format(var2)
'''
    -specifying the number of digits after the decimal point
'''
string = 'pi is appr {:.2f} and 2^2 is {}'.format(var2, var)




#String operations using f strings

string = f'pi is appr {var2} and 2^2 is {var}'
print(string)