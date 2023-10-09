s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

#No se puede modificar

s = set([5, 6, 7, 8])
#s[0] = 3


#Recorrer
s = set([5, 6, 7, 8])
for ss in s:
    print(ss) 

#Metodos
l = set([1, 2])
l.add(3)
print(l)

s = set([1, 2])
s.discard(3)
print(s)

s = set([1, 2])
s.pop()
print(s)

s = set([1, 2])
s.clear()
print(s)

#Otros
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2))