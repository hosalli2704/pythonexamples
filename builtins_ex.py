# map
l = (100,200,300,400)

def func(i):
    return i-10
r1 = map(func, l)

print('r1 =', list(r1))


numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = list(result)
print(numbersSquare)