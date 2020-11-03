from math import *
f=lambda x : (1-x*x)**0.5
true_value=pi/2
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
for n in range(2, 31):
    result=composite_trapezium(n, -1, 1, f)
    print("("+str(log(n))+","+str(-log(abs(true_value-result)))+")")
for n in range(4, 31, 2):
    result=composite_simpsons(n, -1, 1, f)
    print("("+str(log(n))+","+str(-log(abs(true_value-result)))+")")
