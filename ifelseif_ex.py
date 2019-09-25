a = 12
if a == 10:
        print('a equals 10')
elif a > 10:
        print('a is gt than 10')
elif a < 10:
        print('a is less tan 10')

a = 20
if a == 10:
    print('a equals 10')
if a > 10:
    print('a is gt than 10')
if a < 10:
    print('a is less tan 10')


a = 9
if a == 10:
    print('a equals 10')
elif a > 10:
    print('a is gt than 10')
else:
    print('a is less tan 10')


s = 'python'

if s != 'Java':
    print('Not Java')
if not s.startswith('c'):
    print('Not C')
if 'th' in s:
    print('Substring th found')


L1 = [10,20,30]
L2 = L1
L3 = L1.copy()

if L1 == L3:
    print(' are same')
if L1 is L2:
    print('IDS are same')
if 30 in L1:
    print('30 found')