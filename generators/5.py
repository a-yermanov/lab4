def generator(n):
    for i in range (n+1):
        while n>i:
            yield n
            n -= 1

for i in generator(int(input())):
    print (i)