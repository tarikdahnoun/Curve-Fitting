#Lesson 16-Homework 2
#Curve Fitting

from scipy.optimize import curve_fit
import numpy as np
import pylab as py

A = np.loadtxt("C:\\Users\\dahno\\Documents\\PHY251\\Day 16\\sincurve.data")

xi=0
xf=10
N=100
x=np.linspace(xi,xf,N)

xdata=np.zeros(len(A))
ydata=np.zeros(len(A))

for i in range(len(A)):
    xdata[i]=A[i,0]
    ydata[i]=A[i,1]

def func(x,a,b,c):
    return a*np.sin(b*x+c)
    
par, con = curve_fit(func,xdata,ydata)#,p0=ydata[0])
a=par[0]
b=par[1]
period=2*np.pi/b
c=par[2]
y=func(a,b,c,x)

py.annotate('Amplitude='+str(a), xy=(0,-1.7), xytext=(0,-1.7))
py.annotate('Period='+str(period), xy=(0,-2.), xytext=(0,-2.))
py.annotate('Phase Shift='+str(c), xy=(0,-2.3), xytext=(0,-2.3))


for i in range(len(A)-1):
    py.plot(A[i,0],A[i,1],"r.")
    
py.plot(x,y,"-")
py.show()