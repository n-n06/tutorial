'''Lists
-mutable
-can have differetn data types
-can have recurring elements
-can have negative indexex(-1 is the last number and etc.)
-iterable
'''
li = ["a", 5, True]

print(li)

if 5 in li:
    print("yes")
else:
    print("no")

'''
-len() method is the number of elements

-list.append(item) 
-list.insert(index, item)
-list.pop()
    -returns the value of the last element and removes it from the list
-list.remove(item) removes and item
-list.clear() deletes everuthing
-list.reverse() reverses all of the elements
-list.sort()   sorting
-newlist = sorted(oldlist)


-list with recurring elements 
    list = [0]*5     is list = [0,0,0,0,0]

    
-slicing 
    list[i:j:step] from i (incl) to j (exl)

    
-copying: 
    copy = [...]
    copy = old  when the original list is changed, the copied one is changed in the same exact way
-actual copying
    copy = old.copy()
        or
    copy = list(old)

    
-list comprehension
    list = [i for i in list1]
'''
a = [1 , 2, 3, 4, 5]
b = [i*i for i in a]
print(b)

'''
'''




