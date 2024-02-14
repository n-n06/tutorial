from collections import defaultdict
#the whole point of this data structure is that if the key to be printed out or accesed in another way is not in the dictionary we will get a def value of a type
#for example, the default value of int is 0, float is 0.0, a list is [] etc.        
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['a'] += 1
d['c'] += 1
print(d.keys())