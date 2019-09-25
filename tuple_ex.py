# tuple -> class
L = []
L = list()
T1 = (10, 12.5, 'python', ['a', 'b'], (10, 20))
print('T1', T1)
T2 = tuple([10, 20, 30])
print('T2', T2)
print(T1[4])
print(T1[1:3])
i = T1.index(12.5)
c = T1.count('python')
print(i, c)
T3 = (10, 20, 30)
L2 = list(T3)
print('Tuple to List=', L2)
L3 = [10, 20, 30]
T4 = tuple(L3)
print('List to Tuple', T4)

e = enumerate(L3)
print('e=', list(e))
