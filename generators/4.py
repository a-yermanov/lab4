def square(a, b):
    for i in range (a, b+1):
        yield i ** 2

for i in square(int(input()), int(input())):
    print (i)