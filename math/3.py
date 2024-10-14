import math
def polygon():
    n = (int(input("Input number of sides: ")))
    l = (int(input("Input the lenght of a side: ")))
    a=(n*pow(l,2))/4*math.tan(math.pi/n)
    print("The area of the polygon is ", math.ceil(a))
polygon()