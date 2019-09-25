s = 'python'
for a in s:
    print(a)

numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
  sum = sum+val

print("The sum is", sum) # Output: The sum is 28


b = 'Java'
L = [10, 20, 30]

for b in L:
    print('b=', b)


d = {'A': 10, 'B': 20}

for k in d:
    print(k, d[k])
for v in d.values():
    print('v=', v)
for i in d.items():
    print(i, i[0], i[1])
for i, j in d.items():
    print(i, j)


r1 = range(10)
r2 = range(1, 10)
r3 = range(1, 10, 2)

print(list(r1), list(r2), list(r3), sep='\n')


s = 'python'
for j in range(0, len(s)):
    print(s[j], end='')

comp = ['IBM', 'SYN1', 'SAP', 'DELL', 'SYN2']

for c in comp:
    if c.startswith('SYN'):
        print('Found')
        break
else:
    print('NF')
for d in comp:
    if not d.startswith('SYN'):
        continue
    if d.startswith('SYN'):
        print('Hello')
    print('Last')