from functools import reduce
import math

def avg_calc(ls):
    n, mean = len(ls), 0.0

    if n <= 1:
        return ls[0]

    # calculate average
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)

    return mean

def sample_standard_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0

    mean, sd = avg_calc(data), 0.0

    # calculate stan. dev.
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))

    return sd
def slope_calc():
    print("Enter y2")
    y2 = float(input())
    print("Enter y1")
    y1 = float(input())
    print("Enter x2")
    x2 = float(input())
    print("Enter x1")
    x1 = float(input())
    print("Calcution slope")
    m = (y2 - y1) / (x2 - x1)
    print("The Slope {}".format(int(m)))
    return x1,x2,y1,y2,m

def Calculate_the_mean():
    print("Enter a list for x values by comma")
    x = input().split(",")
    xbar = reduce((lambda x, y: int(x) + int(y)),x) / len(x)
    print("mean of the​ x-variable {}".format(xbar))
    print("Enter a list for y values by comma")
    y = input().split(",")
    ybar = reduce((lambda x, y: int(x) + int(y)),y) / len(y)
    print("mean of the​ y-variable {}".format(ybar))
    return x,y,xbar,ybar

def compute_Observation(x1,xbar,sx):
    return round((x1-xbar)/sx,6)


x1,x2,y1,y2,m = slope_calc()
x,y,xbar,ybar = Calculate_the_mean()
print("Calculate the sample standard deviation")
print("Standard Deviation : x ",sample_standard_calc(x))
print("Standard Deviation : y ",sample_standard_calc(y))
sx = sample_standard_calc(x)
sy = sample_standard_calc(y)

xo = compute_Observation(x1,xbar,sx);

print("Compute xo for this observation.")
print (xo)


# print("x {}".format(compute_Observation(9,6.4,2.074)))

# print("y {}".format(compute_Observation(23,15.6,6.189)))


