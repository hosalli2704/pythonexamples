x = 10

def f1():
    x = 13

    def f2():
       # nonlocal x
        x =11
        print("f2", x)
    f2()
    print("f1", x)
f1()
print("Global",x)

print(dir(__builtins__))


def my_func():
	x = 10
	print("Value inside function:",x)

#nonlocal x
x = 2
my_func()
print("Value outside function:",x)


def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")

print(greet.__doc__)