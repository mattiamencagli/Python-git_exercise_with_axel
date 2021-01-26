import sys
import numpy as np
import matplotlib.pyplot as plt

print("\nUsage: you should pass a number to the program to use one of the following functions: ")
print("1: f(x)=x")
print("2: f(x)=x**2")
print("3: f(x)=x**3")
print("4: f(x)=sin(x)")
print("5: f(x)=cos(x)")
print("6: f(x)=tan(x)")
print("7: f(x)=exp(x)")
print("8: f(x)=sqrt(abs(x))")
print("If no number is passed the standard function is: f(x)=x\n")

#handle command line
func_switch = 1
if(len(sys.argv)>1):
	func_switch = int(sys.argv[1])


#fill lists
start=-3
stop=3
step=0.1
xval = np.linspace(start,stop,int((stop-start)/step)+1);

def f1(x):
	return x
def f2(x):
	return x**2
def f3(x):
	return x**3
def f4(x):
	return np.sin(x)
def f5(x):
	return np.cos(x)
def f6(x):
	return np.tan(x)
def f7(x):
	return np.exp(x)
def f8(x):
	return np.sqrt(np.abs(x))
	
	
if func_switch==1:
	yval = f1(xval)
elif func_switch==2:
	yval = f2(xval)
elif func_switch==3:
	yval = f3(xval)
elif func_switch==4:
	yval = f4(xval)
elif func_switch==5:
	yval = f5(xval)
elif func_switch==6:
	yval = f6(xval)
elif func_switch==7:
	yval = f7(xval)
elif func_switch==8:
	yval = f8(xval)
else:
	print("%d IS NOT SUPPORTED STILL, wait for future updates.\n"%func_switch)
	sys.exit()
	


#plot lists
plt.title("Plots")
plt.plot(xval,xval, label="xval")
plt.plot(xval,yval, label="yval")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
