import math
import pylab as pl
i=1
xi1=0
yi1=0
v0=1500
g=9.8
C=1                                                
A=0.1                                                    
rho=1.29                                                    
m=1000                                                  
a=0.0065                                        
alpha=2.5                                    
T0=300
xishu=C*A*rho/(2*m)
vxi1=v0*(math.cos(47*math.pi/180))
vyi1=v0*(math.sin(47*math.pi/180))
xlist1=[x0]
ylist1=[y0]
t1=121
dt1=t1/10000
while i<=10000:
    v1=math.sqrt(vxi1**2+vyi1**2)
    vxi1=vxi1-xishu*((1-a*yi1/T0)**alpha)*v1*vxi1*dt1
    vyi1=vyi1-g*dt1-xishu*((1-a*yi1/T0)**alpha)*v1*vyi1*dt1
    xi1=xi1+vxi1*dt1
    yi1=yi1+vyi1*dt1
    xlist1.append(xi1)
    ylist1.append(yi1)
    i=i+1
pl.figure(figsize=(20, 11))
pl.plot(xlist1,ylist1,'r')
pl.title('Cannon Shell Trajectory',fontsize=40)
pl.xlabel('Horizon Distance',fontsize=26)
pl.ylabel('Height',fontsize=30)
pl.show()
