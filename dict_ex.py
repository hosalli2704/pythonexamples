#dict ->class
D= {'course':'python','dur':5,'loc':'Blr'}
print('D',D)
print(D['course'])
# print(D['abc'])
r1 = D.get('abc','No such key')
print('r1',r1)
# add or upate
