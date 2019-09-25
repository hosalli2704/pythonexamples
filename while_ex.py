a = 0
while a < 10:
    print('a=', a)
    a = a+1

s = 'python'
b = 0
while b < len(s):
    print(s[b])
    b = b + 1

l = [10,20,30]
while l:
    x = l.pop()
    print('processed :', x)


# helpanddir
L = []
print(dir(L), end='\n')
print(help(L.append))

# reading from console
# i = input('Enter Your Name')
# print(i)

a = 10
if a == 10:
    pass