# set -> class
# collections of unordered elements
# NO INDEX
# NO KEY
# MUTABLE
# It can hold only immutable objects (Number, String and Tuples only)
# Its always store the unique values

s1 = {10, 10, 'python', 'py'}
print('Set', s1)
s1.add(20)
s1.add(20)
print('Updated Set',s1)

r1 = s1.remove(20)
print('Updated New Set',s1)
r2 = s1.pop()

print('Updated latest Set',s1)


l1 = [10,10,20,20]
s2 = set(l1)
print('List to Set', s2)


A = {1, 2, 3}
B = {2, 3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A ^ B)

