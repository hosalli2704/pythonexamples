def add():
    a = 10
    b = 20
    c = a + b
    print('c=', c)

def add_numbers(a, b):
  sum = a + b
  print(sum)

add_numbers(4, 5)

def add2():
    a = 10
    b = 20
    c = a + b
    return  a, b, c
    # return
  #  return c

r = add2()
print(r)


# default values

def add4(a, b= 10):
    return  a + b

r5 = add4(10)
print(r5)

r6 = add4(10,20)
print(r6)


#Variable args

def add5(a, b=10 ,*c):
    print('Extra agrs passsed', c)
    r = a + b
    for i in c:
        r = r + i
    return r

r7 = add5(10)
print(r7)

r8 = add5(10, 20, 30, 40 , 50)
print(r8)


# def add()
# def add(a , b)
# def add(a,b=10)
# def add(b=10,a) wrong
