F1 = open('test.txt', 'w')
x = 10
s = 'python\n'
F1.write(str(x)+'\n')
F1.write(s)
F1.flush()

F2 = open('test.txt', 'r')
r1 = F2.read()
print(r1)
F2.seek(0)
r2 = F2.read()
print(r2)

import json
json.dumps([1, 'simple', 'list'])
