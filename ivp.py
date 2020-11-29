from math import *

def f(t, y):
    return sin(y)

true_value=2*atan(tan(0.5)*exp(1))

def euler(y0, h, n, f):
    r=[y0]*(n+1)
    for i in range(1, n+1):
        r[i]=r[i-1]+h*f((i-1)*h, r[i-1])
    return r

def rk2(y0, h, n, f):
    r=[y0]*(n+1)
    for i in range(1, n+1):
        k1=f((i-1)*h, r[i-1])
        k2=f((i-1)*h+h/2, r[i-1]+h/2*k1)
        r[i]=r[i-1]+h*k2
    return r

def rk4(y0, h, n, f):
    r=[y0]*(n+1)
    for i in range(1, n+1):
        k1=f((i-1)*h, r[i-1])
        k2=f((i-1)*h+h/2, r[i-1]+h/2*k1)
        k3=f((i-1)*h+h/2, r[i-1]+h/2*k2)
        k4=f(i*h, r[i-1]+h*k3)
        r[i]=r[i-1]+h*(k1+2*k2+2*k3+k4)/6
    return r

def heun(y0, h, n, f):
    r=[y0]*(n+1)
    for i in range(1, n+1):
        k1=f((i-1)*h, r[i-1])
        k2=f(i*h, r[i-1]+h*k1)
        r[i]=r[i-1]+h*(k1+k2)/2
    return r

def ab3(y0, h, n, f):
    r=[y0]*(n+1)
    g=[f(0, y0)]*(n+1)
    rinit=heun(y0, h, 2, f)
    r[1:3]=rinit[1:3]
    g[1:3]=[f(i*h, r[i]) for i in range(1, 3)]
    for i in range(3, n+1):
        r[i]=r[i-1]+h*(g[i-1]*23/12-g[i-2]*4/3+g[i-3]*5/12)
        g[i]=f(i*h, r[i])
    return r

def plot_error(method):
    for n in range(4, 21):
        y=method(1, 1/n, n, f)[n]
        print("("+str(log(n))+","+str(-log(abs(y-true_value)))+")")
    print("")
    return 0

plot_error(euler)
plot_error(rk2)
plot_error(heun)
plot_error(ab3)
plot_error(rk4)
