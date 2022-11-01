#NOTICE: CURRENTLY WORKS FOR TWO VARIABLES NOW
#WILL SOON UPDATE TO MAKE IT WORK FOR MULTIPLE VARIABLES

import numpy as np
x = np.array(list(map(int, input("Enter values of x: ").split())))
y = np.array(list(map(int, input("Enter values of y: ").split())))
A=np.matrix([[len(x),np.sum(x)],[np.sum(x),np.sum(x**2)]])
X=np.matrix([[np.sum(y)],[np.sum(x*y)]])
b=np.linalg.solve(A,X)
print("y = ",b[0,0],"+",b[1,0],"x")