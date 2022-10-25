from mpmath import *
mp.dps=50               #CHANGE THE PRECISION HERE
x0= str(input("x0: "))
x1= str(input("x1: "))
x0,x1=mpf(x0),mpf(x1)

f= lambda x: x**3 - 5*x -6   # INPUT YOUR FUNCTION HERE

n=int(input("Iterations: "))
for k in range(n):
    y=mpf(str(x1-((x1-x0)*f(x1)/(f(x1)-f(x0)))))
    print(y)
    x0,x1=x1,y
