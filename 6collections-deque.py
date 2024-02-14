from collections import deque

d= deque()

d.append(1)
d.append(2)
d.appendleft(0)
d.appendleft(6)

print(d)

d.popleft()
d.pop()

print(d)

d.extend([3,7,8])
'''elements are added from the left, thus the last element in list becomes the first in the deque e.g. the leftmost element of deque'''
d.extendleft([4,5,6])       

print(d)

'''use rotate(some int) to move the elements in deque some itn amount of time to the right(if some int > 0)'''
d.rotate(2)
print(d)
d.rotate(-4)
print(d)