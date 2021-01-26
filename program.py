import sys
import numpy as np
import matplotlib.pyplot as plt


#handle command line
func_switch = int(sys.argv[1])


#fill lists
start=-5
stop=5
step=0.1
xval = np.linspace(start,stop,int((stop-start)/step)+1);

def f1(x):
	return x
	
if func_switch==1:
	yval = f1(xval)


#plot lists
plt.title("Plots")
plt.plot(xval,xval, label="xval")
plt.plot(xval,yval, label="yval")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
