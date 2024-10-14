def generator(n):
    for i in range (n+1):
        if i % 2 == 0:
            yield i
        else:
            yield ','

for i in generator(int(input())):
    print (i, end='')