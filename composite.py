from math import *
f=lambda x : (1-x*x)**0.5
true_value=pi/6+3**0.5/4

def composite_trapezium(n, a, b, f):
    r=0
    r+=0.5*(f(a)+f(b))
    for i in range(1, n):
        r+=f(((n-i)*a+i*b)/n)
    return r*(b-a)/n

def composite_simpsons(n, a, b, f):
    r=0
    r+=f(a)+f(b)
    for i in range(1, n, 2):
        r+=4*f(((n-i)*a+i*b)/n)
    for i in range(2, n, 2):
        r+=2*f(((n-i)*a+i*b)/n)
    return r*(b-a)/3/n

def composite_gauss(n, a, b, f):
    r=0
    m=int((n+1)/2)
    for i in range(m):
        l0=(i*b+(m-i)*a)/m
        l1=((i+1)*b+(m-i-1)*a)/m
        x0=(l0+l1)/2-(l1-l0)/2/(3**0.5)
        x1=(l0+l1)/2+(l1-l0)/2/(3**0.5)
        r+=f(x0)+f(x1)
    return r*(b-a)/(n+1)

for n in range(2, 31):
    result=composite_trapezium(n, -0.5, 0.5, f)
    print("("+str(log(n))+","+str(-log(abs(true_value-result)))+")")
for n in range(4, 31, 2):
    result=composite_simpsons(n, -0.5, 0.5, f)
    print("("+str(log(n))+","+str(-log(abs(true_value-result)))+")")
for n in range(3, 31, 2):
    result=composite_gauss(n, -0.5, 0.5, f)
    print("("+str(log(n))+","+str(-log(abs(true_value-result)))+")")
