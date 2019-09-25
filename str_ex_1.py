#str -> class
a = 10
b = int(10)
c = 'person'
d = "Person's"
e = '''Person's he c"'''
f = """person"""
g = 'line1\
line 2'
h = """line1
    line 2 """
print(g)
print(h)
i = 'person\`s'
# j=r'C:\Users\User\AppData\Local\Programs\Python\Python36-32\str_ex.py'
k = 'WEL COME'
print(k)
print(len(k))
print(k[1])
print(k[1:6])
print(k[1:])
print(k[:6])
print(k[:])
l = k[:]

print(id(l),id(k))


print(k[1:6:1])
s1 = k[1:3]
s2 = k[6:]

print(k[1:6:2])

print(k[::-1])

r1 = k.startswith('WEL')
print('r1=',r1)

r2 = k.endswith('COME')
print('r2=',r2)

r3 = k.isupper()
print('r3=',r3)



r4 = k.upper()
print('r4=',r4)

#lower,islower

r5 = k.istitle()
print('r5=',r5)

r6 = k.title()
print('r6=',r6)

r7 = k.capitalize()
print('r7=',r7)


line = '#'*40
print(line)

m = 'abc'
r8 = m.isalpha()

print('r8=',r8)
n = '123'
r9 = n.isdigit()

print('r9=',r9)
p = 'abc123'
r10 = p.isalnum()

print('r10=',r10)
r11 = p[-3:].isdigit()

print('r11=',r11)

