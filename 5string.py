'''
String
-immutable
-ordered

-defined by single and double quotes
-use \' to use the single quote in a string defined by single quotes
'''

#multi line string using """"""
string = """hello   
world
i am 
gojo"""
print(string)

#can use \ to avoid multilining when using triple quotes
string = """hello \
world"""
print(string)


'''
-Accessing elements with the same index principle
'''
print(string[4])

'''
-Slicing 
'''
substr = string[::2]
print(substr)

'''
-Concatenation +
'''

'''
-Deleting unnecessary spaces using .strip()
'''

string2 = input()
print(string2.strip())

'''
-lower() upper()
-startswith(substring), endswith(substring)
-find() - the first index of a character or the index of the first character in a substring
-count(char) - number of char
-replace(initial, new)
'''

string2 = string2.replace('a', 'o')


